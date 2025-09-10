Qualitätssicherung in der Softwareentwicklung umfasst strategische Prozesse, Normen und Werkzeuge, um Fehler zu minimieren und stabile Lösungen bereitzustellen. Hier eine strukturierte Übersicht zu den vier Themenfeldern:

---

## 1. Grundlagen der Qualitätssicherung  
**Qualitätssicherungsprozesse** folgen oft dem **Dev-QS-Prod-Modell** (Entwicklung, Qualitätssicherung, Produktion), das den gesamten Softwarelebenszyklus überwacht[2]. Zentrale Modelle sind:  
- **V-Modell**: Phasenweise Validierung und Verifikation  
- **Agile Methoden**: Iterative Qualitätssicherung durch Continuous Integration  
- **Automotive SPICE**: Branchenspezifisches Prozessassessment  

**Metriken zur Messung** umfassen:  
| **Kategorie**         | **Beispiele**                          |  
|------------------------|-----------------------------------------|  
| Entwicklerproduktivität| Durchlaufzeit, Code-Umfang, Work in Progress[3] |  
| Softwareleistung       | Reaktionszeit ($$RT$$), Durchsatz ($$\theta$$), Verfügbarkeit ($$\lambda$$)[3] |  
| Codequalität           | Zyklomatische Komplexität, Duplizierung |  

---

## 2. Dokumentation und Standards  
**Projektdokumentation** sichert Transparenz und dient als **Lessons-Learned**-Grundlage für zukünftige Projekte[4]. Kernbestandteile sind:  
- Anforderungsspezifikationen  
- Architekturentwürfe  
- Testprotokolle  

**Normen**:  
- **ISO 9001**: Fokussiert auf **prozessorientiertes Qualitätsmanagement**, z.B. durch klare Prozessdefinitionen und Kundenorientierung[5].  
- **ISO/IEC 25010**: Definiert **8 Softwarequalitätsmerkmale** wie *Funktionale Eignung*, *Sicherheit* und *Wartbarkeit* mit 31 Submerkmalen[6].  

---

## 3. Review-Methoden  
**Code Reviews** folgen einem strukturierten Ablauf[7][12]:  
1. **Vorbereitung**: Code-Bereitstellung und Checklisten-Erstellung  
2. **Prüfung**:  
   - Funktionalität in allen Anwendungsfällen  
   - Code-Lesbarkeit und Dokumentation  
3. **Rückmeldung**: Dokumentation von Befunden und Nachbesserung  

**Walkthroughs/Inspektionen** dienen der Fehlererkennung in frühen Projektphasen[8]:  
- **Walkthrough**: Informeller Austausch zur Wissensvermittlung  
- **Inspektion**: Formelle Fehleranalyse mit Protokollierung  
- **Vorteile**: Bis zu 60 % Reduktion von Spätfehlern[8]  

---

## 4. Werkzeuge zur Qualitätssicherung  
**Statische Codeanalyse-Tools**:  
| **Tool**       | **Sprachen**          | **Features**                      |  
|----------------|------------------------|-----------------------------------|  
| SonarQube      | Java, C++, Python      | Sicherheitschecks, CI-Integration[9] |  
| Snyk Code      | Python, Java, JavaScript | Echtzeit-Schwachstellenerkennung[13] |  

**Versionskontrollsysteme**:  
| **Kriterium**       | **Git**                                | **SVN**                          |  
|----------------------|----------------------------------------|----------------------------------|  
| **Architektur**      | Dezentral (lokale Repos)               | Zentralisiert (Server-Repo)     |  
| **Stärken**          | Offline-Arbeit, Branching              | Einfache Bedienung, stabile Trunk[10][14] |  
| **Einsatzgebiet**    | Agile Teams mit paralleler Entwicklung | Projekte mit linearer Struktur  |  

Für vertiefende Analysen bieten Quellen wie *SonarQube-Dokumentation* oder *ISO 25010-Standard* detaillierte Leitfäden[6][9].

Citations:
[1] https://blog.ccc-industriesoftware.de/qualitaetssicherung-in-der-softwareentwicklung/
[2] https://www.gecko.de/wissenshub/qualitaetssicherung-in-der-software-entwicklung-so-stellen-sie-die-qualitaet-ihrer-software-sicher/
[3] https://www.computerweekly.com/de/tipp/23-kritische-Metriken-fuer-erfolgreiche-Entwicklungsprojekte
[4] https://www.factro.de/blog/projektdokumentation/
[5] https://www.innolytics.de/was-ist-iso-9001-2015/
[6] https://www.perforce.com/blog/qac/what-is-iso-25010
[7] https://wiki.hshl.de/wiki/index.php/Anleitung_zum_Code_Review
[8] http://software-inspektionen.de
[9] https://www.guru99.com/de/best-static-code-analysis-tools.html
[10] https://nulab.com/learn/software-development/git-vs-svn-version-control-system/
[11] https://vmsoftwarehouse.de/15-masnahmen-zur-qualitatssicherung-in-der-softwareentwicklung
[12] https://clickup.com/de/blog/221480/code-ueberpruefungs-checkliste
[13] https://snyk.io/de/articles/open-source-static-code-analysis/
[14] https://www.ionos.com/digitalguide/websites/web-development/svn-vs-git-comparing-version-control-systems/
[15] https://de.wikipedia.org/wiki/Liste_von_Werkzeugen_zur_statischen_Codeanalyse
[16] https://www.verifysoft.com/de_cmtpp_mscoder.pdf
[17] https://scand.de/unternehmen/blog/wie-man-qualitaet-in-der-softwareentwicklung-sicherstellt/
[18] https://www.computerweekly.com/de/definition/Qualitaetssicherung-QS
[19] https://www.youtube.com/watch?v=jJG-DzWd9e0
[20] https://www.tae.de/weiterbildung/it-digitalisierung/softwareentwicklung/grundlagen-der-qualitaetssicherung-in-der-softwareentwicklung/
[21] https://www.agiliway.com/de/softwareentwicklungsdienste-und-it/software-qualitaetspruefung/
[22] https://de.wikipedia.org/wiki/Softwaremetrik
[23] https://www.jambit.com/kompetenzen/themen/qualitaetssicherung-in-der-softwareentwicklung/
[24] https://de.smartsheet.com/quality-improvement-process
[25] https://users.informatik.haw-hamburg.de/~sarstedt/AKOT/071210-Fleischer-Metriken.pdf
[26] https://qse.ifs.tuwien.ac.at/wp-content/uploads/2007_UBIT_4a.pdf
[27] https://de.linkedin.com/pulse/qualit%C3%A4tssicherung-der-softwareentwicklung-ist-eine
[28] https://inztitut.de/blog/glossar/iso-25010/
[29] https://document360.com/de/blog/projektdokumentation/
[30] https://www.vorest-ag.com/Qualitaetsmanagement-ISO-9001/Wissen/iso-9001-anforderungen
[31] https://www.vde-verlag.de/iec-normen/252317/iso-iec-25010-2023.html
[32] https://de.wikipedia.org/wiki/Projektdokumentation
[33] https://de.wikipedia.org/wiki/ISO_9001
[34] https://iso25000.com/index.php/en/iso-25000-standards/iso-25010
[35] https://www.atlassian.com/de/work-management/knowledge-sharing/documentation/importance-of-documentation
[36] https://advisera.com/9001academy/de/was-ist-iso9001/
[37] https://www.iso.org/obp/ui/
[38] https://www.projektmagazin.de/artikel/einfache-dokumentation-in-der-projektarbeit
[39] https://qualitaetsmanagement.me/qualitaetsmanagement-iso-9001/
[40] https://www.ionos.de/digitalguide/websites/web-entwicklung/code-review/
[41] https://de.wikipedia.org/wiki/Inspektion_(Software-Entwicklung)
[42] https://appmaster.io/de/blog/code-uberprufungen
[43] https://www.gm.th-koeln.de/~winter/images/TAV10WinterOOInspect.pdf
[44] https://www.inovex.de/en/blog/richtlinien-fuer-code-reviews/
[45] https://www.objectsystems.de/qualitaetssicherung-in-softwareprojekten-teil-2.html
[46] https://entwickler.de/programmierung/das-geheimnis-einer-guten-code-review-best-practice-fur-alle
[47] https://de.wikipedia.org/wiki/Review_(Softwaretest)
[48] https://www.basistechnologies.com/de/blog/5-tipps-fuer-erfolgreiche-abap-code-reviews
[49] https://t2informatik.de/wissen-kompakt/walkthrough/
[50] https://www.studysmarter.de/schule/informatik/technische-informatik/code-reviews/
[51] https://de.parasoft.com/solutions/static-code-analysis/
[52] https://www.linode.com/docs/guides/svn-vs-git/
[53] https://www.in-com.com/de/blog/best-static-code-analysis-tools-large-enterprises-2025/
[54] https://stackoverflow.blog/2023/01/09/beyond-git-the-other-version-control-systems-developers-use/
[55] https://xygeni.io/de/blog/top-static-code-analysis-tools/
[56] https://en.wikipedia.org/wiki/List_of_version-control_software
[57] https://www.linux-magazin.de/ausgaben/2012/08/statische-analyse/
[58] https://stackoverflow.com/questions/4550877/learning-about-version-control-systems-git-svn
[59] https://www.verifysoft.com/Auswahlkriterien_Statische_Codeanalysetools.pdf
[60] https://ru.wikipedia.org/wiki/Subversion
[61] https://www.imt.ch/de/expert-blog-detail/was-ist-eine-statische-codeanalyse-und-was-ist-der-anwendungsbereich-davon
[62] https://rightpeoplegroup.com/de/blog/was-gehoert-zum-qs-prozess-ein-kurzer-leitfaden-fuer-den-wichtigen-schritt-in-der-softwareentwicklung
[63] https://www.scnsoft.de/blog/software-qualitaet-metriken
[64] https://www.tenmedia.de/de/glossar/software-qualitatssicherung
[65] https://www.software-mittelstand.info/qualitaetssicherung-in-der-softwareentwicklung-erfolgsfaktoren-und-methoden/
[66] https://dieprojektmanager.com/projektdokumentation-wichtige-grundregeln/
[67] https://www.gbtec.com/de/ressourcen/iso-9001/
[68] https://www.iso.org/standard/35733.html
[69] https://www.ihrprojekt.at/de/blog/tipps/93-kleinigkeiten-dokumentation
[70] https://www.tuvsud.com/de-de/dienstleistungen/auditierung-und-zertifizierung/iso-9001
[71] https://www.it-schulungen.com/wir-ueber-uns/wissensblog/welche-softwaretestmethoden-gibt-es.html
[72] https://www.objectbay.com/blog/was-ist-code-review-inklusive-checkliste
[73] https://qse.ifs.tuwien.ac.at/wp-content/uploads/2007_UBIT_4b.pdf
[74] https://www.johner-institut.de/blog/iec-62304-medizinische-software/code-review/
[75] https://files.ifi.uzh.ch/rerg/amadeus/teaching/courses/software_engineering_hs10/folien/Kapitel_09_Reviews.pdf
[76] https://git-scm.com/docs/git-svn
[77] https://de.parasoft.com/learning-center/static-code-analysis-guide/
[78] https://www.perforce.com/blog/vcs/git-vs-svn-what-difference

---
Antwort von Perplexity: pplx.ai/share