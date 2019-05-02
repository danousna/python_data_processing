# python_data_processing

## Questions sur les données

### Valeur foncière moyenne sur Compiègne

```sql
SELECT SUM(Valeur_fonciere)/COUNT(*) FROM table WHERE Valeur_fonciere IS NOT NULL GROUP BY Valeur_fonciere;
```

### Taille moyenne des terrains.

```sql
SELECT SUM(Surface_terrain)/COUNT(*) FROM table WHERE Surface_terrain IS NOT NULL GROUP BY Surface_terrain;
```

### Avoir le nombre de vente sur 1 mois

```sql
SELECT COUNT(*) FROM table WHERE Nature_mutation = Vente AND MONTH(Date_mutation) = 1 
```

### Rue où il y a le plus de ventes
