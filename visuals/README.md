# Substack Visuals for "El correo que no era para mí"

This directory contains publication-quality visualizations for the Substack article about predatory journal invitations.

## Files

### Primary Visual (for Substack header)
- `pso_score_visual.png` - Bar chart showing PSO Index scores for all 8 cases
  - Dimensions: 1200 x 800 px
  - DPI: 300 (publication quality)
  - Shows perfect classification: 7/8 PSO confirmed, 1/8 legitimate control

### Generation Script
- `../generate_substack_visuals.py` - Python script to regenerate all visuals
  - Requirements: matplotlib, numpy, seaborn
  - Usage: `python3 generate_substack_visuals.py`

### Concept Document
- `../substack_visual_concept.md` - Detailed specifications for professional designer
  - Includes full lifecycle diagram concept
  - Timeline visualization specs
  - Social media format variants

## Usage

### For Substack Article
1. Use `pso_score_visual.png` as the main header image
2. Place immediately after the intro paragraph
3. Add caption: "Perfect classification: 7 of 8 invitations confirmed as Parasitic Spontaneous Order (PSO)"

### For Social Media
1. Crop to 1080 x 1080 px for Instagram/Twitter
2. Add text overlay with key finding
3. Include DOI in image footer

### For Professional Infographic
1. Use `substack_visual_concept.md` as design brief
2. Commission designer on Fiverr/99designs
3. Request deliverables: AI, SVG, PNG (high-res and web-optimized)

## Regeneration

To regenerate visuals with updated data:

```bash
cd /home/user/predatory-invitations-ept
python3 generate_substack_visuals.py
```

This will create/update:
- pso_score_comparison.png
- invitation_timeline.png
- pso_dimensions_heatmap.png
- pso_score_social_media.png

## License

All visuals are licensed under CC BY 4.0, matching the repository license.
When reusing, credit: "Lerer (2026), DOI: 10.5281/zenodo.18853667"
