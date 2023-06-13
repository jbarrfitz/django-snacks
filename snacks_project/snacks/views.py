from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["snacks"] = [
            {
                'title': 'Potato Chips',
                'description': 'Thin, crispy, fried slices of potato, often flavored.',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Kartoffelchips-1.jpg/1024px-Kartoffelchips-1.jpg',
                'reference_url': 'https://en.wikipedia.org/wiki/Chips'
            },
            {
                'title': 'Chocolate Bar',
                'description': 'A sweet, solid candy made from cocoa beans.',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Chocolate_%28blue_background%29.jpg/320px-Chocolate_%28blue_background%29.jpg',
                'reference_url': 'https://en.wikipedia.org/wiki/Chocolate_bar'
            },
            {
                'title': 'Pretzels',
                'description': 'Baked bread product, typically twisted into a knot shape.',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Swedish_%22kringlor%22_%28pretzels%29.jpg/640px-Swedish_%22kringlor%22_%28pretzels%29.jpg',
                'reference_url': 'https://en.wikipedia.org/wiki/Pretzel'
            },
            {
                'title': 'Popcorn',
                'description': 'Popped corn kernels, often flavored or coated in butter.',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Popcorn_up_close_salted_and_air_popped.jpg/220px-Popcorn_up_close_salted_and_air_popped.jpg',
                'reference_url': 'https://en.wikipedia.org/wiki/Popcorn'
            },
            {
                'title': 'Candy Cane',
                'description': 'Cane-shaped hard candy, usually with peppermint flavor.',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/-365_CandyCanes_%2824035106401%29.jpg/640px--365_CandyCanes_%2824035106401%29.jpg',
                'reference_url': 'https://en.wikipedia.org/wiki/Candy_cane'
            },
            {
                'title': 'Cheese Puffs',
                'description': 'Puffed cheese-flavored snacks, often in ball or curl shapes.',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Cheese_puffs.jpg/640px-Cheese_puffs.jpg',
                'reference_url': 'https://en.wikipedia.org/wiki/Cheese_puffs'
            },
            {
                'title': 'Gummy Bears',
                'description': 'Chewy, gelatin-based candies shaped like bears.',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Gummy_bears.jpg/640px-Gummy_bears.jpg',
                'reference_url': 'https://en.wikipedia.org/wiki/Gummy_bears'
            },
            {
                'title': 'Peanut Butter Cups',
                'description': 'Round chocolate cups filled with peanut butter.',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/2021-07-13_20_59_58_A_Reese%27s_Peanut_Butter_Big_Cup_cut_in_two_pieces_in_the_Dulles_section_of_Sterling%2C_Loudoun_County%2C_Virginia.jpg/640px-2021-07-13_20_59_58_A_Reese%27s_Peanut_Butter_Big_Cup_cut_in_two_pieces_in_the_Dulles_section_of_Sterling%2C_Loudoun_County%2C_Virginia.jpg',
                'reference_url': 'https://en.wikipedia.org/wiki/Peanut_butter_cup'
            },
            {
                'title': 'Trail Mix',
                'description': 'A mixture of dried fruits, nuts, and sometimes chocolate.',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Planters-Trail-Mix.jpg/640px-Planters-Trail-Mix.jpg',
                'reference_url': 'https://en.wikipedia.org/wiki/Trail_mix'
            },
            {
                'title': 'Ice Cream Sandwich',
                'description': 'Frozen dessert consisting of ice cream between two cookies.',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Trader_Joe%27s_Sublime_Ice_Cream_Sandwiches.jpg/640px-Trader_Joe%27s_Sublime_Ice_Cream_Sandwiches.jpg',
                'reference_url': 'https://en.wikipedia.org/wiki/Ice_cream_sandwich'
            }
        ]
        return context

class AboutView(TemplateView):
    template_name = 'about.html'