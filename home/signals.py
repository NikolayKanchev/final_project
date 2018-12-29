from django.db.models.signals import post_save
from django.dispatch import receiver
from home.models import Child, Section, Category, ClothingItem


@receiver(post_save, sender=Child)
def create_child_sections(sender, instance, created, **kwargs):
    if created:
        Section.objects.create(child=instance, name='Clothes')
        Section.objects.create(child=instance, name='Shoes')
        Section.objects.create(child=instance, name='Toys')


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


# @receiver(post_save, sender=Child)
# def change_default_size_system(sender, instance, update_fields, **kwargs):
#     print(update_fields)
#     # instance.update(default_size_system=instance.size_system)


