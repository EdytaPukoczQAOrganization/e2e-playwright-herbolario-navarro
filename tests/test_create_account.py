from playwright.sync_api import Page, expect

def test_create_account_with_empty_email(page:Page):
    print("Given the user is on the create your account page for Herbolario Navarro")
    page.goto("https://www.herbolarionavarro.es/customer/account/create/")
    
    print("When the user accepts cookies")
    page.get_by_role("button", name="Aceptar todas").click()
    
    print("And the user fills in the first name field")
    #We put the action .clear to make sure fields are empty before being filled in
    page.get_by_role("textbox", name="Nombre *").clear()
    page.get_by_role("textbox", name="Nombre *").fill("Edy")
    
    print("And the user fills in the last name field")
    #We put the action .clear to make sure fields are empty before being filled in
    page.get_by_role("textbox", name="Apellidos *").clear()
    page.get_by_role("textbox", name="Apellidos *").fill("Guida")
    
    print("And the user fills in the password field and confirms the password")
    #We put the action .clear to make sure fields are empty before being filled in
    page.get_by_role("textbox", name="Contraseña", exact=True).clear()
    page.get_by_role("textbox", name="Contraseña", exact=True).fill("12345Test!")
    page.get_by_role("textbox", name="Confirmar contraseña").clear()
    page.get_by_role("textbox", name="Confirmar contraseña").fill("12345Test!")
    
    print("And the user fills in the zip code field")
    #We put the action .clear to make sure fields are empty before being filled in
    page.get_by_role("textbox", name="Código Postal *").clear()
    page.get_by_role("textbox", name="Código Postal *").fill("28003")

    print("And the user fills in the birth date field")
    page.get_by_role("textbox", name="Fecha de nacimiento *").fill("1997-07-21")
    
    print("And the user fills in the identity number field")
    #We put the action .clear to make sure fields are empty before being filled in
    page.get_by_role("textbox", name="DNI/NIF *").clear()
    page.get_by_role("textbox", name="DNI/NIF *").fill("17183940")
    
    print("And the user accepts the terms and conditions")
    page.locator("#terms-magento-framework-view-element-template-1").check()
    
    print("And the user clicks on the Create Account button")
    page.get_by_role("button", name="Crear cuenta").click()
    
    print("Then the user should see the error message Campo obligatorio")
    expect(page.get_by_text("Campo obligatorio.")).to_be_visible()

def test_create_account_without_accepting_terms_use(page:Page):
    print("Given the user is on the create your account page for Herbolario Navarro")
    page.goto("https://www.herbolarionavarro.es/customer/account/create/")
    
    print("When the user accepts cookies")
    page.get_by_role("button", name="Aceptar todas").click()
    
    print("And the user fills in the first name field")
    #We put the action .clear to make sure fields are empty before being filled in
    page.get_by_role("textbox", name="Nombre *").clear()
    page.get_by_role("textbox", name="Nombre *").fill("Edy")

    print("And the user fills in the last name field")
    #We put the action .clear to make sure fields are empty before being filled in
    page.get_by_role("textbox", name="Apellidos *").clear()
    page.get_by_role("textbox", name="Apellidos *").fill("Guida")
    
    print("When the fills in the email field")
    #We put the action .clear to make sure fields are empty before being filled in
    page.get_by_role("textbox", name="Correo electrónico *").clear()
    page.get_by_role("textbox", name="Correo electrónico *").fill("test@test.com")

    print("And the user fills in the password field and confirms the password")
    #We put the action .clear to make sure fields are empty before being filled in
    page.get_by_role("textbox", name="Contraseña", exact=True).clear()
    page.get_by_role("textbox", name="Contraseña", exact=True).fill("12345Test!")
    page.get_by_role("textbox", name="Confirmar contraseña").clear()
    page.get_by_role("textbox", name="Confirmar contraseña").fill("12345Test!")

    print("And the user fills in the zip code field")
    #We put the action .clear to make sure fields are empty before being filled in
    page.get_by_role("textbox", name="Código Postal *").clear()
    page.get_by_role("textbox", name="Código Postal *").fill("28003")

    print("And the user fills in the birth date field")
    page.get_by_role("textbox", name="Fecha de nacimiento *").fill("1997-07-21")
    
    print("And the user fills in the identity number field")
    #We put the action .clear to make sure fields are empty before being filled in
    page.get_by_role("textbox", name="DNI/NIF *").clear()
    page.get_by_role("textbox", name="DNI/NIF *").fill("17183940")
    
    print("And the user clicks on the Create account button")
    page.get_by_role("button", name="Crear cuenta").click()
    
    print("Then the user should see errror message Campo obligatorio and the account should not be created")
    expect(page.get_by_text("Campo obligatorio.")).to_be_visible()

def test_create_account_without_dni_field(page:Page):
    print("Given the user is on the create your account page for Herbolario Navarro")
    page.goto("https://www.herbolarionavarro.es/customer/account/create/")
    
    print("When the user accepts the cookies")
    page.get_by_role("button", name="Aceptar todas").click()
    
    print("And the user fills in the first name field")
    #We put the action .clear to make sure fields are empty before being filled in
    page.get_by_role("textbox", name="Nombre *").clear()
    page.get_by_role("textbox", name="Nombre *").fill("Edy")
    
    print("And the user fills in the last name field")
    #We put the action .clear to make sure fields are empty before being filled in
    page.get_by_role("textbox", name="Apellidos *").clear()
    page.get_by_role("textbox", name="Apellidos *").fill("Guida")

    print("When the fills in the email field")
    #We put the action .clear to make sure fields are empty before being filled in
    page.get_by_role("textbox", name="Correo electrónico *").clear()
    page.get_by_role("textbox", name="Correo electrónico *").fill("test@test.com")

    print("And the user fills in the password field and confirms the password")
    #We put the action .clear to make sure fields are empty before being filled in
    page.get_by_role("textbox", name="Contraseña", exact=True).clear()
    page.get_by_role("textbox", name="Contraseña", exact=True).fill("12345Test!")
    page.get_by_role("textbox", name="Confirmar contraseña").clear()
    page.get_by_role("textbox", name="Confirmar contraseña").fill("12345Test!")

    print("And the user fills in the zip code field")
    #We put the action .clear to make sure fields are empty before being filled in
    page.get_by_role("textbox", name="Código Postal *").clear()
    page.get_by_role("textbox", name="Código Postal *").fill("28003")

    print("And the user fills in the birth date field")
    page.get_by_role("textbox", name="Fecha de nacimiento *").fill("1997-07-21")
    
    print("And the user accepts the terms and conditions")
    page.locator("#terms-magento-framework-view-element-template-1").check()
    
    print("And the user clicks on the Create account button")
    page.get_by_role("button", name="Crear cuenta").click()
    
    print("Then the user should see the error message Campo obligatorio and the form should not be sent")
    expect(page.get_by_text("Campo obligatorio.")).to_be_visible()