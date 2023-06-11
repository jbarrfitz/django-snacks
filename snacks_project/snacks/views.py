from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["snacks"] = [
    {
        'title': 'Chips',
        'description': 'Thin, crispy slices of potato or corn, often flavored.',
        'image': 'https://example.com/chips.jpg',
        'reference_url': 'https://en.wikipedia.org/wiki/Chips'
    },
    {
        'title': 'Chocolate Bar',
        'description': 'A sweet, solid candy made from cocoa beans.',
        'image': 'https://example.com/chocolate_bar.jpg',
        'reference_url': 'https://en.wikipedia.org/wiki/Chocolate_bar'
    },
    {
        'title': 'Pretzels',
        'description': 'Baked bread product, typically twisted into a knot shape.',
        'image': 'https://example.com/pretzels.jpg',
        'reference_url': 'https://en.wikipedia.org/wiki/Pretzel'
    },
    {
        'title': 'Popcorn',
        'description': 'Popped corn kernels, often flavored or coated in butter.',
        'image': 'https://example.com/popcorn.jpg',
        'reference_url': 'https://en.wikipedia.org/wiki/Popcorn'
    },
    {
        'title': 'Candy Cane',
        'description': 'Cane-shaped hard candy, usually with peppermint flavor.',
        'image': 'https://example.com/candy_cane.jpg',
        'reference_url': 'https://en.wikipedia.org/wiki/Candy_cane'
    },
    {
        'title': 'Cheese Puffs',
        'description': 'Puffed cheese-flavored snacks, often in ball or curl shapes.',
        'image': 'https://example.com/cheese_puffs.jpg',
        'reference_url': 'https://en.wikipedia.org/wiki/Cheese_puffs'
    },
    {
        'title': 'Gummy Bears',
        'description': 'Chewy, gelatin-based candies shaped like bears.',
        'image': 'https://example.com/gummy_bears.jpg',
        'reference_url': 'https://en.wikipedia.org/wiki/Gummy_bears'
    },
    {
        'title': 'Peanut Butter Cups',
        'description': 'Round chocolate cups filled with peanut butter.',
        'image': 'https://example.com/peanut_butter_cups.jpg',
        'reference_url': 'https://en.wikipedia.org/wiki/Peanut_butter_cup'
    },
    {
        'title': 'Trail Mix',
        'description': 'A mixture of dried fruits, nuts, and sometimes chocolate.',
        'image': 'https://example.com/trail_mix.jpg',
        'reference_url': 'https://en.wikipedia.org/wiki/Trail_mix'
    },
    {
        'title': 'Ice Cream Sandwich',
        'description': 'Frozen dessert consisting of ice cream between two cookies.',
        'image': 'https://example.com/ice_cream_sandwich.jpg',
        'reference_url': 'https://en.wikipedia.org/wiki/Ice_cream_sandwich'
    }
]


        return context

class AboutView(TemplateView):
    template_name = 'about.html'