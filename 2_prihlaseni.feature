Feature: Přihlášení/odhlášení
  Scenario: Zobrazení přihlášení
	Given hlavní stránka opencart
	When uživatel klikne na tlačítko "My Account"
	And klikne tlačítko "Login"
	Then otevře se záložka Account/Login

  Scenario: Neúspěšné přihlášení
  	Given formulář Přihlášení
	And zadaný účet neexistuje
	When uživatel vyplní jakékoli údaje do "E-Mail Address" a "Password"
	And zmáčkne tlačítko Login
	Then zobrazí se Chyba

  Scenario: Úspěšné přihlášení
  	Given formulář Přihlášení
	And zadaný účet existuje
	When uživatel vyplní správné údaje do "E-Mail Address" a "Password"
	And zmáčkne tlačítko Login
	Then zobrazí se obrazovka "Account"

  Scenario: Odhlášení
  	Given přihlášený uživatel
	When uživatel zmáčkne tlačítko "Logout"
	Then zobrazí se obrazovka "Account Logout"

  Scenario: Zapomenuté heslo
  	Given formulář Přihlášení
	When uživatel zmáčkne tlačítko "Forgotten Password"
	Then zobrazí se obrazovka "Forgot Your Password?"