//
// aufgabe4.c
//

///// includes /////

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


///// defines /////

// Length
#define MAX_LIST_LENGTH (1024 * 5)
#define MAX_NAME_LENGTH (255)
#define MAX_EMAIL_LENGTH (255)


///// structs /////

typedef struct
{
    long id;
    char szName[MAX_NAME_LENGTH];
    char szEmail[MAX_EMAIL_LENGTH];
    KUNDE_ts *next;
} KUNDE_ts;

///// global /////

KUNDE_ts *g_psKundenListe;


///// prototypes /////

void kundeHinzufuegen(KUNDE_ts *psKundenListe, int id, char *psName, char *psEmail);
KUNDE_ts *kundeSuchen(KUNDE_ts *psKundenListe, int id);
void kundeEntfernen(KUNDE_ts *psKundenListe, int id);


///// funtions /////

int main()
{
    g_psKundenListe = NULL;

    kundeHinzufuegen (g_psKundenListe, 1, "Jakob", "jakob@email");
    kundeSuchen (g_psKundenListe, 1);
    kundeEntfernen(g_psKundenListe, 1);
    
    return 0;
}

///// private functions /////

void kundeHinzufuegen(KUNDE_ts *psKundenListe, int id, char *psName, char *psEmail)
{
    KUNDE_ts *psTmp;
    psTmp = NULL;

    if (psKundenListe = NULL)
    {
        psTmp = (KUNDE_ts *)malloc (sizeof(KUNDE_ts));
    }
    else
    {
        psTmp = psKundenListe->next;

        while (psTmp != NULL)
        {
            if (psTmp->id == id)
            {
                printf ("Error id schon vergeben\n");
                return;
            }

            psTmp = psTmp->next;
        }

        psTmp = (KUNDE_ts *)malloc (sizeof(KUNDE_ts));
    }

    psTmp->id = id;
    strcpy(psTmp->szEmail, psEmail);
    strcpy(psTmp->szName, psName);
    psTmp->next = NULL;
    printf("kunde hinzugefügt\n");
}


KUNDE_ts *kundeSuchen(KUNDE_ts *psKundenListe, int id)
{
    KUNDE_ts *psTmp;
    psTmp = NULL;

     if (psKundenListe = NULL)
     {
        printf("Error");
        return NULL;
     }

    psTmp = psKundenListe;

    while (psTmp != NULL)
    {
        if (psTmp->id == id)
        {
           printf("kunde gefunden: %s %s", psTmp->szEmail, psTmp->szName);
           return psTmp;
        }

        psTmp = psTmp->next;
    }

    printf("Error nichts gefunden\n");
    return NULL;
}

void kundeEntfernen(KUNDE_ts *psKundenListe, int id)
{
    KUNDE_ts *psTmp, *psPrev;
    
    psPrev = NULL;
    psTmp = NULL;

    if (psKundenListe = NULL)
    {
       printf("Error");
       return;
    }

    psTmp = psKundenListe;
    psPrev = psTmp;

    while (psTmp != NULL)
    {
        if (psTmp->id == id)
        {
            psPrev->next = psTmp->next;
            free(psTmp);
            printf("kunde entfernt\n");
            return;
        }

        psPrev = psTmp;
        psTmp = psTmp->next;
    }
}
