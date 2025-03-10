from playwright.sync_api import Page, expect

def test_visit_menu_links(page: Page):
    print("Given the user is visiting the homepage https://www.herbolarionavarro.es/")
    #Navegación, abrir la url en el navegador
    page.goto("https://www.herbolarionavarro.es/")
   
    print("When the user accepts the cookies")
    #Localizamos el elemento por texto, utilizamos el exact=True porque se refiere al exact match. Si no lo incluimos, el sistema lo tratará como contiene
    ##page.get_by_text("Aceptar todas", exact = True).click()

    page.get_by_role("button", name = "Aceptar todas").click()

    print("And clicks on the Nuestras Marcas element on the menu")
    #Localizamos el elemento por rol (button,link,heading) y por texto exacto para los enlaces principales
    page.get_by_role("link", name = "Nuestras Marcas", exact = True).click()
    print("And clicks on the Nuestras Destacados on the menu")
    page.get_by_role("link", name = "Destacados", exact = True).click()
    ##print("And clicks on the Alimentación element on the menu")
    ##page.get_by_role("link", name = "Alimentación", exact = True).click()
    ##print("And clicks on the Dietética y Nutrición element on the menu")
    ##page.get_by_role("link", name = "Dietética y Nutrición", exact = True).click()
    ##print("And clicks on the Cosmética Natural y Ecológica element on the menu")
    ##page.get_by_role("link", name = "Cosmética Natural y Ecológica ", exact = True).click()
    print("And clicks on the Higiene element on the menu")
    page.get_by_role("link", name = "Higiene", exact = True).click()
    print("And clicks on the Frescos element on the menu")
    page.get_by_role("link", name = "Frescos", exact = True).click()
    ##print("And clicks on the Bebé y Niño element on the menu")
    ##page.get_by_role("link", name = "Bebé y Niño", exact = True).click()
    ##print("And clicks on the Hogar element on the menu")
    ##page.get_by_role("link", name = "Hogar", exact = True).click()
    ##print("And clicks on the Ofertas element on the menu")
    ##page.get_by_role("link", name = "Ofertas", exact = True).click()