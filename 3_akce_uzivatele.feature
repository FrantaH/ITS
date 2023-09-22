Feature: Spravování účtu
  Scenario: Změna základních informací
  	Given záložka Account/Edit Information
	When uživatel změní hodnoty
	And klikne tlačítko "continue"
	Then změní se hodnoty na nové

  Scenario: Změna hesla
  	Given formulář na změnu hesla
	When uživatel vyplní nové heslo
	And klikne tlačítko "continue"
	Then heslo se změní na nové
	And na obrazovce se objeví potvrzené úspěchu

  Scenario: Pokus smazat poslední (defaultní) adresu
  	Given obrazovka záznamů Address
	And uživatel obsahuje pouze a jen jednu adresu
	When uživatel zmáčkne tlačítko "Delete"
	Then vypíše Warning, že není možné smazat defaultní adresu
	And adresa zůstane původní

  Scenario: Změna změna wish listu
  	Given záložka Account/My Wish List
	And wish list obsahuje první položku
	When zmáčkne červený křížek
	Then první položka se smaže z wish listu
	And vypíše se potvrzení úspěchu

  Scenario: Zobrazení detailu objednávky
  	Given záložka Account/Order History
	And objednaná položka 1
	When uživatel zmáčkne červené tlačítko s okem
	Then zobrazí se detail k položce 1

  Scenario: Znovu objednání
  	Given záložka Account/Order History/Order Information
	And prázdný "košík"
	When uživatel klikne modré tlačítko s košíkem
	Then do košíku se přidá jedna položka