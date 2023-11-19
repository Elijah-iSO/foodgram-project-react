from django.db.models import F, Sum
from django.http import HttpResponse

from recipes.constants import FILENAME
from recipes.models import Ingredient, RecipeIngredient, ShoppingCart
from users.models import Follow


def get_subscribed(obj, request):
    if request is None or request.user.is_anonymous:
        return False
    return Follow.objects.filter(user=request.user, author=obj).exists()


def create_recipe_ingredient(recipe, ingredients_data):
    ingredients = []
    for ingredient_data in ingredients_data:
        ingredient_id = ingredient_data['ingredient']['id']
        amount = ingredient_data['amount']
        ingredient = Ingredient.objects.get(id=ingredient_id)
        existing_recipe_ingredient = RecipeIngredient.objects.filter(
            recipe=recipe,
            ingredient=ingredient_id)
        if existing_recipe_ingredient.exists():
            existing_recipe_ingredient.update(amount=F('amount') + amount)
        else:
            recipe_ingredient = RecipeIngredient(
                recipe=recipe,
                ingredient=ingredient,
                amount=amount
            )
            ingredients.append(recipe_ingredient)
    RecipeIngredient.objects.bulk_create(ingredients)


def collect_shopping_cart(request):
    shopping_cart_recipes = ShoppingCart.objects.filter(user=request.user)
    recipe_ids = shopping_cart_recipes.values_list('recipe_id', flat=True)

    ingredient_quantities = RecipeIngredient.objects.filter(
        recipe__id__in=recipe_ids
    ).values('ingredient__name', 'ingredient__measurement_unit').annotate(
        total_amount=Sum('amount')
    )

    file_content = "\n".join(
        [f"{item['ingredient__name']} "
         f"({item['ingredient__measurement_unit']}) "
         f"— {item['total_amount']}" for item in ingredient_quantities]
    )

    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename={FILENAME}'
    response.write(file_content)

    return response
