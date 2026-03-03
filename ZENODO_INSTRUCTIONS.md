# Instrucciones para Depósito en Zenodo

Este repositorio está completamente preparado para ser depositado en Zenodo y obtener un DOI permanente.

---

## Archivos de Metadata Incluidos

✅ **CITATION.cff** - Formato Citation File Format (estándar GitHub/Zenodo)  
✅ **.zenodo.json** - Metadata específico para Zenodo  
✅ **README.md** - Documentación completa con placeholders para DOI  
✅ **LICENSE** - CC BY 4.0 (compatible con Zenodo)

---

## Pasos para Depositar en Zenodo

### Opción A: Desde GitHub (RECOMENDADO)

1. **Habilitar integración GitHub-Zenodo:**
   - Ir a https://zenodo.org/account/settings/github/
   - Click en "Sync now" para sincronizar repositorios
   - Activar el switch para `predatory-invitations-as-extended-phenotype`

2. **Crear un Release en GitHub:**
   ```bash
   # En GitHub web interface:
   # - Ir a Releases
   # - Click "Create a new release"
   # - Tag: v1.0.0
   # - Title: "Spontaneous Parasitic Order v1.0.0 - Complete Corpus"
   # - Description: "First complete release with all 8 cases documented"
   # - Click "Publish release"
   ```

3. **Zenodo creará automáticamente:**
   - DOI permanente
   - Página de depósito
   - Badge para README

4. **Actualizar README con DOI real:**
   - Copiar DOI de Zenodo (formato: 10.5281/zenodo.XXXXXXX)
   - Reemplazar placeholders `XXXXXXX` en README.md
   - Reemplazar en CITATION.cff
   - Reemplazar en .zenodo.json
   - Commit y push cambios

### Opción B: Upload Manual a Zenodo

1. **Crear archivo ZIP:**
   ```bash
   cd /home/user
   zip -r pso-repo-v1.0.0.zip predatory-invitations-ept/ -x "*.git*"
   ```

2. **Subir a Zenodo:**
   - Ir a https://zenodo.org/deposit/new
   - Upload ZIP
   - Completar metadata manualmente (usa .zenodo.json como referencia)

3. **Publicar y obtener DOI**

4. **Actualizar README** (igual que Opción A, paso 4)

---

## Metadata Ya Configurado

### Información Básica
- **Título:** Spontaneous Parasitic Order: Predatory Publishing as Extended Phenotype
- **Autor:** Ignacio Adrián Lerer
- **Tipo:** Dataset
- **Licencia:** CC BY 4.0
- **Versión:** 1.0.0

### Keywords (10 total)
- predatory publishing
- extended phenotype theory
- spontaneous order
- institutional parasitism
- academic integrity
- evolutionary game theory
- peer review
- open science
- PSO index
- scientific misconduct

### Descripción
Ver `.zenodo.json` para descripción HTML completa preparada.

### Referencias
4 referencias clave incluidas en metadata:
1. Dawkins - Extended Phenotype (1982)
2. Hayek - Law, Legislation and Liberty (1973)
3. Beall - Nature paper (2012)
4. Grudniewicz et al. - Nature paper (2019)

---

## Contenido del Depósito

**29 archivos totales:**

### Archivos principales (5)
- README.md (documentación completa)
- LICENSE (CC BY 4.0)
- CITATION.cff (metadata citación)
- .zenodo.json (metadata Zenodo)
- .gitignore (configuración)

### Data/ (4 archivos)
- README.md
- invitations_corpus.csv (8 casos)
- coding_matrix.csv (patrones binarios)
- pso_index_scores.csv (scores calculados)

### Analysis/ (2 archivos)
- README.md
- pso_identification.py (script Python)

### Emails/ (9 archivos)
- README.md
- email_01_jcllt_bonview.md (LEGÍTIMO - control)
- email_02_ijfes_academix.md (template error)
- email_03_statistics_exploresci.md (Gmail sender)
- email_04_journalism_oask.md (acepta PPTs)
- email_05_jhecr_198usd.md (precio explícito)
- email_06_economics_glint.md (phantom follow-up)
- email_07_ai_academicvision.md (catch-all scope)
- email_08_geosciences_premier.md (extreme mismatch)

### Supplementary/ (4 archivos)
- case_study_diago.md (validación externa)
- stress_test_cases.md (objeciones teóricas)
- multidomain_extension.md (aplicaciones cross-domain)

### Extensions/ (2 archivos)
- README.md
- citation_rings.md (propuesta extensión)

### Paper/ (2 archivos)
- README.md
- abstract.md

---

## Checklist Post-Depósito

Una vez obtenido el DOI de Zenodo:

- [ ] Actualizar README.md con DOI real
- [ ] Actualizar CITATION.cff con DOI real
- [ ] Actualizar .zenodo.json con DOI real
- [ ] Crear badge de Zenodo para README
- [ ] Commit cambios: `git commit -m "Update with Zenodo DOI"`
- [ ] Push a GitHub: `git push origin main`
- [ ] Añadir DOI al perfil ORCID (si existe)
- [ ] Compartir en redes académicas (Twitter, LinkedIn, Substack)

---

## Badge para README

Después de obtener DOI, agregar al README:

```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
```

Reemplazar `XXXXXXX` con número real de Zenodo.

---

## Cómo Citar Este Trabajo (Post-DOI)

**BibTeX:**
```bibtex
@dataset{lerer2026parasitic,
  author = {Lerer, Ignacio Adrián},
  title = {Spontaneous Parasitic Order: Predatory Publishing as Extended Phenotype},
  year = {2026},
  publisher = {Zenodo},
  version = {1.0.0},
  doi = {10.5281/zenodo.XXXXXXX},
  url = {https://doi.org/10.5281/zenodo.XXXXXXX}
}
```

**APA:**
```
Lerer, I. A. (2026). Spontaneous Parasitic Order: Predatory Publishing as Extended Phenotype (Version 1.0.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.XXXXXXX
```

---

## Razón del Depósito en Zenodo

Como se indica en el README:

> **Nota:** Dado que SSRN no acepta más papers del autor, este trabajo se preserva exclusivamente en GitHub y Zenodo para garantizar acceso permanente y citabilidad.

Zenodo proporciona:
- ✅ DOI permanente (citación académica)
- ✅ Preservación a largo plazo (CERN)
- ✅ Versioning (futuras actualizaciones)
- ✅ Integración con GitHub (sincronización automática)
- ✅ Búsqueda académica (indexado en OpenAIRE, etc.)

---

## Versiones Futuras

Si se actualiza el repositorio:

1. Hacer cambios en GitHub
2. Crear nuevo Release (v1.1.0, v2.0.0, etc.)
3. Zenodo creará nuevo DOI para nueva versión
4. DOI anterior permanece accesible
5. Concept DOI agrupa todas las versiones

---

## Contacto para Problemas

Si hay problemas con el depósito:
- Email: adrian@lerer.com.ar
- GitHub Issues: https://github.com/adrianlerer/predatory-invitations-as-extended-phenotype/issues

---

**Estado:** Repositorio listo para depósito  
**Fecha de preparación:** Marzo 3, 2026  
**Próximo paso:** Crear Release v1.0.0 en GitHub y obtener DOI de Zenodo
