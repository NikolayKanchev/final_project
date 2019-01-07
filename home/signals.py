import os

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from home.models import Child, Section, Category, Photo, Item


@receiver(post_save, sender=Child)
def create_child_sections(sender, instance, created, **kwargs):
    if created:
        Section.objects.create(child=instance, name='Clothes')
        Section.objects.create(child=instance, name='Shoes')
        Section.objects.create(child=instance, name='Toys')

        Photo.objects.create(child=instance, file=None)


@receiver(post_save, sender=Section)
def create_section_categories(sender, instance, created, **kwargs):
    if created:
        if instance.name == "Clothes":
            Category.objects.create(section=instance, name='Bodies')
            Category.objects.create(section=instance, name='Blouses')
            Category.objects.create(section=instance, name='Trousers')
            Category.objects.create(section=instance, name='Shorts')
        elif instance.name == "Shoes":
            Category.objects.create(section=instance, name='Boots')
            Category.objects.create(section=instance, name='Sneakers')
            Category.objects.create(section=instance, name='Sandals')
        elif instance.name == "Toys":
            Category.objects.create(section=instance, name='Baby')
            Category.objects.create(section=instance, name='Outdoor')
            Category.objects.create(section=instance, name='Musical')


@receiver(pre_save, sender=Photo)
def delete_old_file(sender, instance, **kwargs):
    if instance.pk:
        old_file = Photo.objects.get(pk=instance.pk).file
        if old_file:
            os.remove(old_file.path)


@receiver(post_save, sender=Item)
def create_more_items_based_on_the_amount(sender, instance, created, **kwargs):
    if created:

        if instance.amount > 1:
            for i in range(instance.amount - 1):
                Item.objects.create(
                    category=instance.category,
                    picture=instance.picture,
                    note=instance.note,
                    brand=instance.brand,
                    condition=instance.condition,
                    sex=instance.sex,
                    season=instance.season,
                    color=instance.color,
                    price=instance.price,
                    amount=1,
                    clothing_size=instance.clothing_size,
                    shoe_size=instance.shoe_size,
                )


