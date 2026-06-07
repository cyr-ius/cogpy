# cogpy

Client Python asynchrone pour l'[API COG](https://portail-api.insee.fr) (Code Officiel Géographique) de l'INSEE — le référentiel officiel des entités géographiques françaises.

## Installation

```bash
pip install cogpy
```

## Prérequis

- Python >= 3.10
- [aiohttp](https://docs.aiohttp.org/) >= 3.8.1

## Utilisation rapide

```python
import asyncio
from cogpy import COG, COGException

async def main():
    api = COG()

    try:
        # Récupérer une commune par son code INSEE
        paris = await api.async_get_commune("75056")
        print(paris)

        # Chercher toutes les communes nommées "Bordeaux"
        communes = await api.async_get_all_communes(filtre_nom="Bordeaux")
        print(communes)

        # Obtenir les départements d'une région
        deps = await api.async_get_region_descendants("11", type="Departement")
        print(deps)

    except COGException as err:
        print(f"Erreur : {err}")
    finally:
        await api.async_close()

asyncio.run(main())
```

## API

### `COG(session=None, timeout=120)`

Classe cliente principale. Accepte optionnellement une `aiohttp.ClientSession` existante et un délai d'expiration en secondes.

### Paramètres communs

| Paramètre         | Type  | Description                                                           |
| ----------------- | ----- | --------------------------------------------------------------------- |
| `code`            | `str` | Code de l'entité géographique                                         |
| `date`            | `str` | Date au format `YYYY-MM-DD` pour interroger l'état historique         |
| `type`            | `str` | Filtre sur le type d'entité descendante (ex. `"Commune"`, `"Region"`) |
| `filtre_nom`      | `str` | Filtre partiel sur le nom (3 caractères minimum)                      |
| `date_projection` | `str` | Date de projection future au format `YYYY-MM-DD`                      |

### Méthodes disponibles par entité

Chaque entité expose tout ou partie des opérations suivantes :

| Opération           | Description                                  |
| ------------------- | -------------------------------------------- |
| `get_<entité>`      | Récupère une entité par son code             |
| `get_all_<entités>` | Liste toutes les entités                     |
| `_ascendants`       | Entités parentes (région, département…)      |
| `_descendants`      | Entités enfants (communes, arrondissements…) |
| `_precedents`       | Entités prédécesseures (historique)          |
| `_suivants`         | Entités successeures (historique)            |
| `_projetes`         | Projection de l'entité à une date future     |

---

#### Pays

| Méthode                                                  | Description                                        |
| -------------------------------------------------------- | -------------------------------------------------- |
| `async_get_pays(code, date=None)`                        | Pays par son code (5 chiffres commençant par `99`) |
| `async_get_all_pays(date=None, type=None)`               | Liste de tous les pays                             |
| `async_get_pays_descendants(code, date=None, type=None)` | Territoires descendants                            |
| `async_get_pays_precedents(code, date=None)`             | Pays prédécesseurs                                 |
| `async_get_pays_suivants(code, date=None)`               | Pays successeurs                                   |

---

#### Région

| Méthode                                                    | Description                      |
| ---------------------------------------------------------- | -------------------------------- |
| `async_get_region(code, date=None)`                        | Région par son code (2 chiffres) |
| `async_get_all_regions(date=None)`                         | Liste de toutes les régions      |
| `async_get_region_ascendants(code, date=None, type=None)`  | Entités ascendantes              |
| `async_get_region_descendants(code, date=None, type=None)` | Entités descendantes             |
| `async_get_region_precedents(code, date=None)`             | Régions prédécesseures           |
| `async_get_region_suivants(code, date=None)`               | Régions successeures             |
| `async_get_region_projetes(code, date_projection)`         | Régions projetées                |

---

#### Département

| Méthode                                                         | Description                    |
| --------------------------------------------------------------- | ------------------------------ |
| `async_get_departement(code, date=None)`                        | Département par son code       |
| `async_get_all_departements(date=None)`                         | Liste de tous les départements |
| `async_get_departement_ascendants(code, date=None, type=None)`  | Entités ascendantes            |
| `async_get_departement_descendants(code, date=None, type=None)` | Entités descendantes           |
| `async_get_departement_precedents(code, date=None)`             | Départements prédécesseurs     |
| `async_get_departement_suivants(code, date=None)`               | Départements successeurs       |
| `async_get_departement_projetes(code, date_projection)`         | Départements projetés          |

---

#### Commune

| Méthode                                                         | Description                               |
| --------------------------------------------------------------- | ----------------------------------------- |
| `async_get_commune(code, date=None)`                            | Commune par son code INSEE (5 caractères) |
| `async_get_all_communes(date=None, type=None, filtre_nom=None)` | Liste de toutes les communes              |
| `async_get_commune_ascendants(code, date=None, type=None)`      | Entités ascendantes                       |
| `async_get_commune_descendants(code, date=None, type=None)`     | Entités descendantes                      |
| `async_get_commune_precedents(code, date=None)`                 | Communes prédécesseures                   |
| `async_get_commune_suivants(code, date=None)`                   | Communes successeures                     |
| `async_get_commune_projetes(code, date_projection)`             | Communes projetées                        |

---

#### Commune associée

| Méthode                                                             | Description                            |
| ------------------------------------------------------------------- | -------------------------------------- |
| `async_get_commune_associee(code, date=None)`                       | Commune associée par son code          |
| `async_get_all_communes_associees(date=None, filtre_nom=None)`      | Liste de toutes les communes associées |
| `async_get_commune_associee_ascendants(code, date=None, type=None)` | Entités ascendantes                    |
| `async_get_commune_associee_precedents(code, date=None)`            | Communes associées prédécesseures      |
| `async_get_commune_associee_projetes(code, date_projection)`        | Communes associées projetées           |
| `async_get_commune_associee_suivants(code, date=None)`              | Communes associées successeures        |

---

#### Commune déléguée

| Méthode                                                             | Description                            |
| ------------------------------------------------------------------- | -------------------------------------- |
| `async_get_commune_deleguee(code, date=None)`                       | Commune déléguée par son code          |
| `async_get_all_communes_deleguees(date=None, filtre_nom=None)`      | Liste de toutes les communes déléguées |
| `async_get_commune_deleguee_ascendants(code, date=None, type=None)` | Entités ascendantes                    |
| `async_get_commune_deleguee_precedents(code, date=None)`            | Communes déléguées prédécesseures      |
| `async_get_commune_deleguee_projetes(code, date_projection)`        | Communes déléguées projetées           |
| `async_get_commune_deleguee_suivants(code, date=None)`              | Communes déléguées successeures        |

---

#### EPCI (Intercommunalité)

| Méthode                                                  | Description                           |
| -------------------------------------------------------- | ------------------------------------- |
| `async_get_epci(code, date=None)`                        | EPCI par son code SIREN               |
| `async_get_all_epcis(date=None)`                         | Liste de toutes les intercommunalités |
| `async_get_epci_ascendants(code, date=None, type=None)`  | Entités ascendantes                   |
| `async_get_epci_descendants(code, date=None, type=None)` | Entités descendantes                  |
| `async_get_epci_precedents(code, date=None)`             | EPCI prédécesseurs                    |
| `async_get_epci_suivants(code, date=None)`               | EPCI successeurs                      |
| `async_get_epci_projetes(code, date_projection)`         | EPCI projetés                         |

---

#### Arrondissement

| Méthode                                                            | Description                                  |
| ------------------------------------------------------------------ | -------------------------------------------- |
| `async_get_arrondissement(code, date=None)`                        | Arrondissement par son code (3-4 caractères) |
| `async_get_all_arrondissements(date=None)`                         | Liste de tous les arrondissements            |
| `async_get_arrondissement_ascendants(code, date=None, type=None)`  | Entités ascendantes                          |
| `async_get_arrondissement_descendants(code, date=None, type=None)` | Entités descendantes                         |
| `async_get_arrondissement_precedents(code, date=None)`             | Arrondissements prédécesseurs                |
| `async_get_arrondissement_suivants(code, date=None)`               | Arrondissements successeurs                  |
| `async_get_arrondissement_projetes(code, date_projection)`         | Arrondissements projetés                     |

---

#### Arrondissement municipal (Paris, Lyon, Marseille)

| Méthode                                                                     | Description                                          |
| --------------------------------------------------------------------------- | ---------------------------------------------------- |
| `async_get_arrondissement_municipal(code, date=None)`                       | Arrondissement municipal par son code (5 caractères) |
| `async_get_all_arrondissements_municipaux(date=None)`                       | Liste de tous les arrondissements municipaux         |
| `async_get_arrondissement_municipal_ascendants(code, date=None, type=None)` | Entités ascendantes                                  |
| `async_get_arrondissement_municipal_precedents(code, date=None)`            | Arrondissements municipaux prédécesseurs             |
| `async_get_arrondissement_municipal_projetes(code, date_projection)`        | Arrondissements municipaux projetés                  |
| `async_get_arrondissement_municipal_suivants(code, date=None)`              | Arrondissements municipaux successeurs               |

---

#### Canton

| Méthode                                                   | Description                                       |
| --------------------------------------------------------- | ------------------------------------------------- |
| `async_get_canton(code, date=None)`                       | Canton par son code (4 chiffres métropole, 5 DOM) |
| `async_get_all_cantons(date=None)`                        | Liste de tous les cantons                         |
| `async_get_canton_ascendants(code, date=None, type=None)` | Entités ascendantes                               |
| `async_get_canton_communes(code, date=None)`              | Communes incluses dans le canton                  |
| `async_get_canton_precedents(code, date=None)`            | Cantons prédécesseurs                             |
| `async_get_canton_suivants(code, date=None)`              | Cantons successeurs                               |
| `async_get_canton_projetes(code, date_projection)`        | Cantons projetés                                  |

---

#### Canton ou ville

| Méthode                                                                              | Description                         |
| ------------------------------------------------------------------------------------ | ----------------------------------- |
| `async_get_canton_ou_ville(code, date=None)`                                         | Canton-ou-ville par son code        |
| `async_get_all_cantons_et_villes(date=None)`                                         | Liste de tous les cantons-et-villes |
| `async_get_canton_ou_ville_ascendants(code, date=None, type=None)`                   | Entités ascendantes                 |
| `async_get_canton_ou_ville_descendants(code, date=None, type=None, filtre_nom=None)` | Entités descendantes                |
| `async_get_canton_ou_ville_precedents(code, date=None)`                              | Cantons-ou-villes prédécesseurs     |
| `async_get_canton_ou_ville_suivants(code, date=None)`                                | Cantons-ou-villes successeurs       |
| `async_get_canton_ou_ville_projetes(code, date_projection)`                          | Cantons-ou-villes projetés          |

---

#### Aire d'attraction des villes 2020

| Méthode                                                                    | Description                                   |
| -------------------------------------------------------------------------- | --------------------------------------------- |
| `async_get_aire_attraction_villes(code, date=None)`                        | Aire d'attraction par son code (3 caractères) |
| `async_get_all_aires_attraction_villes(date=None)`                         | Liste de toutes les aires                     |
| `async_get_aire_attraction_villes_descendants(code, date=None, type=None)` | Entités descendantes                          |

---

#### Bassin de vie 2022

| Méthode                                                        | Description                               |
| -------------------------------------------------------------- | ----------------------------------------- |
| `async_get_bassin_vie(code, date=None)`                        | Bassin de vie par son code (5 caractères) |
| `async_get_all_bassins_vie(date=None, filtre_nom=None)`        | Liste de tous les bassins de vie          |
| `async_get_bassin_vie_descendants(code, date=None, type=None)` | Entités descendantes                      |

---

#### Circonscription territoriale

| Méthode                                                                          | Description                                 |
| -------------------------------------------------------------------------------- | ------------------------------------------- |
| `async_get_circonscription_territoriale(code, date=None)`                        | Circonscription par son code (5 caractères) |
| `async_get_all_circonscriptions_territoriales(date=None)`                        | Liste de toutes les circonscriptions        |
| `async_get_circonscription_territoriale_ascendants(code, date=None, type=None)`  | Entités ascendantes                         |
| `async_get_circonscription_territoriale_descendants(code, date=None, type=None)` | Entités descendantes                        |
| `async_get_circonscription_territoriale_precedents(code, date=None)`             | Circonscriptions prédécesseures             |
| `async_get_circonscription_territoriale_suivants(code, date=None)`               | Circonscriptions successeures               |
| `async_get_circonscription_territoriale_projetes(code, date_projection)`         | Circonscriptions projetées                  |

---

#### Collectivité d'outre-mer

| Méthode                                                                    | Description                       |
| -------------------------------------------------------------------------- | --------------------------------- |
| `async_get_collectivite_outre_mer(code, date=None)`                        | Collectivité par son code         |
| `async_get_all_collectivites_outre_mer(date=None)`                         | Liste de toutes les collectivités |
| `async_get_collectivite_outre_mer_ascendants(code, date=None, type=None)`  | Entités ascendantes               |
| `async_get_collectivite_outre_mer_descendants(code, date=None, type=None)` | Entités descendantes              |
| `async_get_collectivite_outre_mer_precedents(code, date=None)`             | Collectivités prédécesseures      |
| `async_get_collectivite_outre_mer_suivants(code, date=None)`               | Collectivités successeures        |
| `async_get_collectivite_outre_mer_projetes(code, date_projection)`         | Collectivités projetées           |

---

#### District

| Méthode                                                      | Description                 |
| ------------------------------------------------------------ | --------------------------- |
| `async_get_district(code, date=None)`                        | District par son code       |
| `async_get_all_districts(date=None)`                         | Liste de tous les districts |
| `async_get_district_ascendants(code, date=None, type=None)`  | Entités ascendantes         |
| `async_get_district_descendants(code, date=None, type=None)` | Entités descendantes        |
| `async_get_district_precedents(code, date=None)`             | Districts prédécesseurs     |
| `async_get_district_suivants(code, date=None)`               | Districts successeurs       |
| `async_get_district_projetes(code, date_projection)`         | Districts projetés          |

---

#### Unité urbaine 2020

| Méthode                                                           | Description                         |
| ----------------------------------------------------------------- | ----------------------------------- |
| `async_get_unite_urbaine(code, date=None)`                        | Unité urbaine par son code          |
| `async_get_all_unites_urbaines(date=None, filtre_nom=None)`       | Liste de toutes les unités urbaines |
| `async_get_unite_urbaine_descendants(code, date=None, type=None)` | Entités descendantes                |

---

#### Zone d'emploi 2020

| Méthode                                                         | Description                        |
| --------------------------------------------------------------- | ---------------------------------- |
| `async_get_zone_emploi(code, date=None)`                        | Zone d'emploi par son code         |
| `async_get_all_zones_emploi(date=None, filtre_nom=None)`        | Liste de toutes les zones d'emploi |
| `async_get_zone_emploi_descendants(code, date=None, type=None)` | Entités descendantes               |

---

### `async_close()`

Ferme la session HTTP. À appeler en fin d'utilisation (ou via `finally`).

## Exceptions

| Exception              | Description                                |
| ---------------------- | ------------------------------------------ |
| `COGException`         | Exception de base                          |
| `HttpRequestError`     | Erreur réseau ou de communication          |
| `TimeoutExceededError` | Délai d'attente dépassé                    |
| `RequestException`     | Réponse HTTP en erreur retournée par l'API |

## Licence

GPL-3.0-or-later — voir le fichier [LICENSE](LICENSE).
