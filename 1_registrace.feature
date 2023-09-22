Feature: Registrace
  Scenario: Zobrazení možností registrace
	Given hlavní stránka opencart
	When uživatel klikne na tlačítko "My Account"
	Then objeví se okénko s možností registrace a loginu
	
  Scenario: Otevření registračního okna	
	Given okenko s možností registrace a loginu
	When uživatel klikne na tlačítko "register"
	Then otevře se formulář s registračními údaji
	
  Scenario: Zadání formuláře
	Given formulář registrace
	When uživatel vyplní všechny nutné (hvězdičkou označené) údaje
	And označí checkbox "I have read and agree to the Privacy Policy"
	And klikne na tlačítko "Continue"
	Then stránka s potvrzením se zobrazí
	And uživatel je přihlášen

  Scenario: Zadání chybného formuláře
	Given formulář registrace
	When uživatel nevyplní nic
	And klikne tlačítko "Continue"
	Then označí se všechny nutné položky jako chybné

  Scenario: Zadání chybného telefoního čísla
	Given formulář registrace
	when uživatel vyplní validní informace kromě telefonu (písmena)
	Then chyba v telefonním čísle