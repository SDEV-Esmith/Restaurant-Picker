import tkinter as tk
import random as rd

#Class for getting a random restaurant
class ChooseRestaurant:
    #Initialize restaurant dictionaries
    def __init__(self, low, medium, high):
        self.low = low
        self.medium = medium
        self.high = high

    #Get random restaurant
    def low_price_chosen(self):
        random_rest = rd.choice(list(self.low.keys()))
        return random_rest
    def medium_price_chosen(self):
        random_rest = rd.choice(list(self.medium.keys()))
        return random_rest
    def high_price_chosen(self):
        random_rest = rd.choice(list(self.high.keys()))
        return random_rest

class FetchImage:
    def __init__(self, random_rest, low, medium, high):
        self.random_rest = random_rest
        self.low = low
        self.medium = medium
        self.high = high


    def fetch_low_image(self, random_rest, low):
        """Get image from low price list"""
        chosen_image = self.low.get(random_rest)
        return chosen_image


    def fetch_medium_image(self, random_rest, medium):
        """Get image from medium price list"""
        chosen_image = self.medium.get(random_rest)
        return chosen_image


    def fetch_high_image(self, random_rest, high):
        """Get image from high price list"""
        chosen_image = self.high.get(random_rest)
        return chosen_image

#Class for handling our application
class Application:

    #Initialize root and welcome screen
    def __init__(self, root):
        self.root = root
        self.images = self.initialize_images()
        self.low_price, self.medium_price, self.high_price = self.initialize_dict(self.images)
        self.welcome_screen()

    #Initialize images
    def initialize_images(self):
        '''Read in all images'''
        #Initialize empty dictionary
        images = {}
        try:
                #Key is "restaurant_image" and value is the image read in
                images["great_divide_image"] = tk.PhotoImage(file="great_divide_image.png")
                images["john_stew_image"] = tk.PhotoImage(file="john_stew_image.png")
                images["la_eskina_image"] = tk.PhotoImage(file="la_eskina.png")
                images["bocca_image"] = tk.PhotoImage(file="bocca_image.png")
                images["freddys_image"] = tk.PhotoImage(file="freddys_image.png")
                images["mass_avenue_image"] = tk.PhotoImage(file="mass_avenue_image.png")
                images["tin_roof_image"] = tk.PhotoImage(file="tin_roof_image.png")
                images["goodfellas_image"] = tk.PhotoImage(file="goodfellas_image.png")
                images["aw_image"] = tk.PhotoImage(file="aw_image.png")
                images["culvers_image"] = tk.PhotoImage(file="culvers_image.png")
                images["punch_bowl_image"] = tk.PhotoImage(file="punch_bowl_image.png")
                images["inferno_image"] = tk.PhotoImage(file="inferno_image.png")
                images["shapiros_image"] = tk.PhotoImage(file="shapiros_image.png")
                images["taxman_image"] = tk.PhotoImage(file="taxman_image.png")
                images["district_tap_image"] = tk.PhotoImage(file="district_tap_image.png")
                images["futuro_image"] = tk.PhotoImage(file="futuro_image.png")
                images["connors_image"] = tk.PhotoImage(file="connors_image.png")
                images["festiva_image"] = tk.PhotoImage(file="festiva_image.png")
                images["tenth_street_image"] = tk.PhotoImage(file="tenth_street_image.png")
                images["fresco_image"] = tk.PhotoImage(file="fresco_image.png")
                images["vida_image"] = tk.PhotoImage(file="vida_image.png")
                images["fountain_room_image"] = tk.PhotoImage(file="fountain_room_image.png")
                images["harry_and_izzys_image"] = tk.PhotoImage(file="harry_and_izzys_image.png")
                images["bluebeard_image"] = tk.PhotoImage(file="bluebeard_image.png")
                images["prime_image"] = tk.PhotoImage(file="prime_image.png")
                images["st_elmo_image"] = tk.PhotoImage(file="st_elmo_image.png")
                images["beholder_image"] = tk.PhotoImage(file="beholder_image.png")
                images["ocean_prime_image"] = tk.PhotoImage(file="ocean_prime_image.png")
                images["union_fifty_image"] = tk.PhotoImage(file="union_fifty_image.png")
                images["mesh_image"] = tk.PhotoImage(file="mesh_image.png")
        #Handle errors for missing images
        except tk.TclError as error:
            print(f"Error loading images {error}")
        return images

    #Initialize dictionaries for price tiers
    def initialize_dict(self, images):
        '''Initialize dictionaries key being the restaurant name and get image being the value'''
        low_price = {
            "The Great Divide": images.get("great_divide_image"),
            "John’s Famous Stew": images.get("john_stew_image"),
            "La Eskina Indy": images.get("la_eskina_image"),
            "Bocca": images.get("bocca_image"),
            "Freddy’s": images.get("freddys_image"),
            "Mass Avenue Pub": images.get("mass_avenue_image"),
            "Tin Roof": images.get("tin_roof_image"),
            "Goodfellas Pizzaria": images.get("goodfellas_image"),
            "A&W Restaurant": images.get("aw_image"),
            "Culver’s": images.get("culvers_image")
        }

        medium_price = {
            "Punch Bowl Social" : images.get("punch_bowl_image"),
            "The Inferno Room" : images.get("inferno_image"),
            "Shapiro's Delicatessen" : images.get("shapiros_image"),
            "TaxMan Cityway" : images.get("taxman_image"),
            "The District Tap" : images.get("tenth_street_image"),
            "Futuro" : images.get("futuro_image"),
            "Connor's Kitchen + Bar" : images.get("connors_image"),
            "Festiva" : images.get("festiva_image"),
            "10th Street Diner" : images.get("tenth_street_image"),
            "Fresco Italian Café on the Canal" : images.get("fresco_image")
        }

        high_price = {
            "Vida": images.get("vida_image"),
            "The Fountain Room": images.get("fountain_room_image"),
            "Harry & Izzy's": images.get("harry_and_izzys_image"),
            "BlueBeard": images.get("bluebeard_image"),
            "Prime 47": images.get("prime_image"),
            "St. Elmo Steak House": images.get("st_elmo_image"),
            "Beholder": images.get("beholder_image"),
            "Ocean Prime": images.get("ocean_prime_image"),
            "Union 50": images.get("union_fifty_image"),
            "Mesh": images.get("mesh_image")
        }
        return low_price, medium_price, high_price


    def welcome_screen(self):
        """Display welcome screen"""
        # Making widgets
        self.welcome_title = tk.Label(self.root, text = 'Having trouble deciding on a restaurant?', font = ("Arial", 20, "bold"))

        #Start button with anon function that calls on_start function and passes dictionaries
        self.start_button = tk.Button(self.root, text="Start!", font = ("Arial", 20, "bold"), bg = "dodger blue", fg = "white", command = self.on_start, width = 10, height = 2)

        #Arranging widgets
        self.welcome_title.place(relx = .5, rely = .25, anchor = "center")
        self.start_button.place(relx = .5, rely = .5, anchor = "center")

    def on_start(self):
        """Runs once start is clicked. This screen displays price tiers."""
        #Delete widgets
        self.welcome_title.destroy()
        self.start_button.destroy()
        self.welcome_title.destroy()
        self.start_button.destroy()

        #Initialize Choose_rest
        rest_picker = ChooseRestaurant(self.low_price, self.medium_price, self.high_price)

        #Add widgets
        start_title = tk.Label(self.root, text = 'Choose a price tier', font = "Arial 16 bold", width = 20, height = 2)
        low_price_button = tk.Button(
            self.root,
            font="Arial 16 bold",
            text = "$",
            bg="dodger blue", fg="white",
            width = 10, height = 2,
            command=lambda: self.handle_restaurant_and_image(rest_picker.low_price_chosen(),"low")
        )
        medium_price_button = tk.Button(
            self.root,
            font = "Arial 16 bold",
            text="$$",
            bg="dodger blue", fg="white",
            width = 10, height = 2,
            command=lambda: self.handle_restaurant_and_image(rest_picker.medium_price_chosen(),"low")
        )
        high_price_button = tk.Button(
            self.root,
            font="Arial 16 bold",
            text="$$$",
            bg="dodger blue", fg="white",
            width = 10, height = 2,
            command=lambda: self.handle_restaurant_and_image(rest_picker.high_price_chosen(),"high")
        )

        #Arrange widgets
        start_title.place(relx = .5, rely = .15, anchor = "center")
        low_price_button.place(relx = .5, rely = .4, anchor = "center")
        medium_price_button.place(relx = .5, rely = .6, anchor = "center")
        high_price_button.place(relx = .5, rely = .8, anchor = "center")

    def handle_restaurant_and_image(self, chosen_restaurant, price_tier):
        """Gets image and restaurant name """
        pass

def main():
    """Main function"""
    # Initialize root
    root = tk.Tk()

    # Set the title
    root.title('Indianapolis restaurant chooser')

    # Set dimensions
    root.geometry('600x600+300+300')
    root.resizable(False, False)
    background_image = tk.PhotoImage(file = "Restaurant Images/background_image.png")
    background_label = tk.Label(root, image = background_image)
    background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    root.background_image = background_image

    #Initialize Application with root as parameter
    app = Application(root)

    #Executes our program and waits for clicks
    root.mainloop()


if __name__ == "__main__":
    main()