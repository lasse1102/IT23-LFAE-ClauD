/* Aufgabe 3.1 */
BEGIN
	SELECT sum(V.Umsatz) as Umsatz
	FROM Verkäufe V, Produkte P
	WHERE P.produkt_id = V.produkt_id
	GROUP BY P.Kategorie
END
/*-------------------------------------------------*/

/* Aufgabe 3.2 (In plain SQL funktioniert Top(5)) */
BEGIN
	SELECT TOP(5) P.produktname AS Produkt, P.preis AS Preis, SUM(V.umsatz) AS Gesamtumsatz
	FROM Produkte P, Verkäufe V
	WHERE P.produkt_id = V.produkt_id
	GROUP BY P.produktname
	ORDER BY V.umsatz
END
/*-------------------------------------------------*/
