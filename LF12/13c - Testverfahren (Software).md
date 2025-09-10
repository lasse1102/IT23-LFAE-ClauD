Softwaretests sind ein zentraler Bestandteil der Qualitätssicherung und umfassen verschiedene Methoden, Stufen und Werkzeuge. Hier eine strukturierte Übersicht der wichtigsten Konzepte:

---

## 1. Testarten und Teststufen  
### **Unit-, Integrations-, System- und Abnahmetests**  
Die vier primären Teststufen nach ISTQB sind:  
- **Unit-Tests (Komponententest):**  
  Prüfen einzelne Codeeinheiten (z. B. Funktionen) auf korrekte Funktionalität. Entwickler führen sie mit White-Box-Methoden durch[1][3][11].  
- **Integrationstests:**  
  Testen das Zusammenspiel mehrerer Komponenten, um Schnittstellenfehler zu identifizieren. Häufig als Black-Box-Tests durch Tester durchgeführt[1][3][11].  
- **Systemtests:**  
  Bewerten das vollständige System auf funktionale und nichtfunktionale Anforderungen (z. B. Performance)[1][11].  
- **Abnahmetests:**  
  Validieren, ob das System vertragliche Anforderungen erfüllt, oft durch Endnutzer oder Kunden[1][11].  

### **Funktionale vs. nichtfunktionale Tests**  
| **Kriterium**       | **Funktionale Tests**               | **Nichtfunktionale Tests**         |
|----------------------|-----------------------------------|-----------------------------------|
| **Fokus**            | Funktionalität (z. B. Login)      | Leistung, Benutzerfreundlichkeit  |
| **Basis**            | Kundenanforderungen               | Kundenexpectations                |
| **Beispiel**         | Prüfung der Suchfunktion          | Ladezeit des Dashboards (<2s)     |
| **Automatisierbarkeit** | Manuell möglich                  | Oft automatisiert erforderlich[2] |  

---

## 2. Testmethoden  
### **Black-Box- vs. White-Box-Testing**  
| **Aspekt**           | **Black-Box**                     | **White-Box**                     |
|----------------------|-----------------------------------|-----------------------------------|
| **Codekenntnis**     | Keine                            | Vollständig                       |
| **Ziel**             | Validierung von Spezifikationen  | Analyse interner Code-Pfade       |
| **Beispiele**        | Funktionstests, Lasttests        | Unit-Tests, Code-Coverage-Analyse |
| **Testdurchführung** | Externe Tester                   | Entwickler[3][4]                 |  

### **Test Driven Development (TDD)**  
Ein iterativer Entwicklungsansatz mit drei Phasen:  
1. **Red Phase:** Schreiben eines fehlschlagenden Tests für eine neue Funktion.  
2. **Green Phase:** Implementierung minimalen Codes, um den Test zu bestehen.  
3. **Refactor:** Optimierung des Codes ohne Funktionsänderung[5].  
TDD fördert robusten Code und senkt Fehlerkosten durch frühe Fehlererkennung[5][13].  

---

## 3. Testplanung und Auswertung  
### **Testplan-Erstellung**  
- **Ziele:** Festlegung von Testumfang, -strategien und Erfolgskriterien[6][7].  
- **Ressourcenplanung:** Zuordnung von Personal (Tester, Entwickler), Tools und Testumgebungen[7].  
- **Zeitplanung:** Schätzung des Aufwands pro Testphase (z. B. 170 Mannstunden für Testdesign)[7].  

### **Dokumentation von Testergebnissen**  
- Testfälle werden mit Eingabedaten, Aktionen und erwarteten Ergebnissen protokolliert (z. B. "Anmeldung mit gültigen Daten führt zur Startseite")[6].  
- Risikoanalysen und Abweichungen werden festgehalten, um Nachverfolgbarkeit zu gewährleisten[6].  

---

## 4. Automatisierte Tests  
### **Werkzeuge**  
- **Selenium:** Automatisierung von Browserinteraktionen für Webanwendungen, unterstützt parallele Tests und diverse Sprachen[8][12][15].  
- **JUnit:** Framework für Unit-Tests in Java, integrierbar in CI/CD-Pipelines[12].  

### **CI/CD-Pipelines**  
- **Continuous Integration (CI):** Automatisierte Builds und Tests bei jedem Code-Commit[9][13].  
- **Continuous Deployment (CD):** Automatisierte Auslieferung getesteter Codeänderungen in Produktion[9][13].  
- **Vorteile:** Frühe Fehlererkennung, schnellere Releases und konsistente Prozesse[9][14].  

---

Diese Strukturierung deckt die zentralen Aspekte moderner Softwaretestverfahren ab, von der Planung bis zur Automatisierung. Die Wahl der Methoden hängt stets von Projektanforderungen, Risiken und Ressourcen ab.

Citations:
[1] https://www.guru99.com/de/levels-of-testing.html
[2] https://www.guru99.com/de/functional-testing-vs-non-functional-testing.html
[3] https://www.guru99.com/de/unit-test-vs-integration-test.html
[4] https://www.security-insider.de/der-unterschied-zwischen-black-box-und-white-box-test-a-18f8432acb561c2016671b9d45ccae58/
[5] https://www.browserstack.com/guide/what-is-test-driven-development
[6] https://www.studysmarter.de/ausbildung/ausbildung-in-it/fachinformatiker-anwendungsentwicklung/softwaretest-planung/
[7] https://www.guru99.com/de/test-planning.html
[8] https://www.andagon.com/blog/selenium-in-der-testautomatisierung
[9] https://www.redhat.com/en/topics/devops/what-cicd-pipeline
[10] https://www.assets.dpunkt.de/leseproben/13487/Einf%C3%BChrung%20in%20die%20Testautomatisierung%20und%20ihre%20Ziele.pdf
[11] https://www.peterjohann-consulting.de/teststufen/
[12] https://www.7p-solutions-consulting.com/blog/testautomatisierung-blog/die-top-7-testautomatisierungstools-fur-effiziente-ablaufe/
[13] https://about.gitlab.com/topics/ci-cd/
[14] https://www.7p-solutions-consulting.com/blog/testautomatisierung-entmystifiziert-ein-leitfaden-fuer-einsteiger/
[15] https://www.testautomatisierung.org/lexikon/selenium/
[16] https://aqua-cloud.io/de/the-only-integration-testing-guide-you-need/
[17] https://de.wikipedia.org/wiki/Softwaretest
[18] https://www.zaptest.com/de/nicht-funktionales-testen-was-ist-das-arten-ansaetze-tools-und-mehr
[19] https://www.atlassian.com/de/continuous-delivery/software-testing/types-of-software-testing
[20] https://www.peterjohann-consulting.de/testpyramide/
[21] https://www.loadview-testing.com/de/blog/arten-von-softwaretests-unterschiede-und-beispiele/
[22] https://www.reddit.com/r/embedded/comments/14lhaq8/integration_test_vs_system_test/?tl=de
[23] https://www.richard-seidl.com/de/blog/teststufen
[24] https://fg-tav.gi.de/fileadmin/FG/TAV/36.TAV/EsGibtKeineNichtfunktionalenTests.pdf
[25] https://appmaster.io/de/blog/arten-von-softwaretests
[26] https://www.atlassian.com/continuous-delivery/software-testing/types-of-software-testing
[27] https://www.johner-institut.de/blog/iec-62304-medizinische-software/funktionale-und-nicht-funktionale-anforderungen/
[28] https://www.practitest.com/resource-center/article/black-box-vs-white-box-testing/
[29] https://testbee.com/en/black-box-vs-white-box-testing-en/
[30] https://www.testrail.com/blog/test-driven-development/
[31] https://clickup.com/de/blog/220921/black-box-white-box-grey-box-pruefung
[32] https://www.peterjohann-consulting.de/black-box-und-white-box-test/
[33] https://en.wikipedia.org/wiki/Test-driven_development
[34] https://www.youtube.com/watch?v=00PO7GFsSzs
[35] https://clickup.com/blog/black-box-white-box-grey-box-testing/
[36] https://www.testautomatisierung.org/lexikon/test-driven-development-tdd/
[37] https://thecodest.co/de/blog/3-unterschiede-zwischen-black-box-und-white-box-tests-aufdecken/
[38] https://www.it-agile.de/agiles-wissen/agile-entwicklung/was-ist-testgetriebene-entwicklung/
[39] https://turingpoint.de/blog/testmethoden-white-black-und-grey-box-welche-ist-die-richtige-fuer-mich/
[40] https://aqua-cloud.io/de/create-software-testing-plan/
[41] https://de.wikipedia.org/wiki/Software_Test_Documentation
[42] https://www.testbench.com/de/testplanung/
[43] https://www.hettwer-beratung.de/konzepte/testkonzept/testdokumentation/
[44] https://www.guru99.com/de/test-plan-for-project.html
[45] https://www.planta.de/blog/projekmanagement-ressourcenplanung/
[46] https://www.guru99.com/de/testing-documentation.html
[47] https://learn.microsoft.com/de-de/azure/devops/test/create-a-test-plan?view=azure-devops
[48] https://www.planview.com/de/resources/guide/resource-management-software/resource-planning/
[49] https://de.linkedin.com/advice/0/what-most-effective-ways-document-test-sqlte?lang=de
[50] https://informatik-pruefung.de/kurse/softwaretests/lektionen/testplanung-und-testdesign/
[51] https://www.hettwer-beratung.de/konzepte/testkonzept/testplan/
[52] https://nativdigital.com/testautomatisierung/
[53] https://www.testing-board.com/testautomatisierung-tools/
[54] https://dinext-group.com/wiki/ci-cd/
[55] https://www.testautomatisierung.org/lexikon/testwerkzeuge/
[56] https://www.qytera.de/blog/beste-testautomatisierung-tools-automation
[57] https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment
[58] https://q-centric.com/blogs/die-besten-tools-fuer-die-testautomatisierung-2021
[59] https://q-centric.com/blogs/die-besten-tools-fuer-die-testautomatisierung-2024
[60] https://en.wikipedia.org/wiki/CI/CD
[61] https://www.qytera.de/blog/testautomatisierung-tipps-goldene-regeln
[62] https://aqua-cloud.io/de/continuous-automation-testing-tools/
[63] https://www.splunk.com/de_de/blog/learn/ci-cd-devops-pipeline.html
[64] https://clickup.com/de/blog/269252/funktionale-und-nicht-funktionale-tests
[65] https://www.unimedia.tech/de/unterscheidung-zwischen-unit-testing-und-integrationstest/
[66] http://wwwlehre.dhbw-stuttgart.de/~hoyer/ePapers/Wikipedia/SWE1-SoftwareTest_Wikipedia.pdf
[67] https://prometteursolutions.com/blog/de/funktionale-vs-nicht-funktionale-tests-die-auffalligen-unterschiede-verstehen/
[68] https://testbee.com/software-qualitaetssicherung/black-white-box-testing/
[69] https://qcademy.de/schwarz-auf-weiss-die-unterschiede-zwischen-white-box-und-black-box-testing/
[70] https://testdriven.io/test-driven-development/
[71] https://www.computerweekly.com/de/definition/White-Box-Test
[72] https://www.bitgrip.com/blog/software-testing-die-wichtigsten-methoden-im-praxis-check
[73] https://martinfowler.com/bliki/TestDrivenDevelopment.html
[74] https://www.studysmarter.de/ausbildung/ausbildung-in-it/fachinformatiker-anwendungsentwicklung/testdokumentation/
[75] https://aqua-cloud.io/de/test-plan-management/
[76] https://qse.ifs.tuwien.ac.at/wp-content/uploads/08P_Planung_wid_20031209.pdf
[77] https://aqua-cloud.io/de/effective-test-documentation/
[78] https://aqua-cloud.io/de/testing-strategy/
[79] https://parm.com/testmanagement-in-projekten/
[80] https://www.redhat.com/en/topics/devops/what-is-ci-cd

---
Antwort von Perplexity: pplx.ai/share