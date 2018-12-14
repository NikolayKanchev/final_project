from django.db.models.signals import post_save
from django.dispatch import receiver
from home.models import Child, Section, Category


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
            Category.objects.create(section=instance, name='Bodies', num_items=0)
            Category.objects.create(section=instance, name='Blouses', num_items=0)
            Category.objects.create(section=instance, name='Trousers', num_items=0)
            Category.objects.create(section=instance, name='Shorts', num_items=0)
        elif instance.name == "Shoes":
            Category.objects.create(section=instance, name='Boots', num_items=0)
            Category.objects.create(section=instance, name='Sneakers', num_items=0)
            Category.objects.create(section=instance, name='Sandals', num_items=0)
        elif instance.name == "Toys":
            Category.objects.create(section=instance, name='Baby', num_items=0)
            Category.objects.create(section=instance, name='Outdoor', num_items=0)
            Category.objects.create(section=instance, name='Musical', num_items=0)
