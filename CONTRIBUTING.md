# Panduan Kontribusi
## Branch Strategy
Proyek ini menggunakan strategi branching berikut:
- main: Branch produksi yang stabil, berisi kode yang siap di-deploy
- develop: Branch pengembangan utama, berisi fitur yang sedang dalam pengembangan
- feature/[nama-fitur]: Branch untuk pengembangan fitur tertentu
- bugfix/[nama-bug]: Branch untuk memperbaiki bug
- hotfix/[nama-issue]: Branch untuk hotfix pada production

## Workflow
1. Buat branch baru dari develop:
```bash
git checkout develop
git pull origin develop
git checkout -b feature/nama-fitur
```
2. Kerjakan perubahan pada branch feature
3. Commit perubahan dengan pesan deskriptif:
```bash
git add .
git commit -m "Feat: Menambahkan fitur XYZ"
```
4. Push branch ke remote repository:
```bash
git push origin feature/nama-fitur
```
5. Buat Pull Request (PR) dari branch feature ke branch develop
6. Setelah review dan approval, branch feature akan di-merge ke develop
7. Secara berkala, develop akan di-merge ke main melalui release

## Konvensi Commit
Format pesan commit:
- Feat: Untuk fitur baru
- Fix: Untuk bug fix
- Docs: Untuk perubahan pada dokumentasi
- Style: Untuk perubahan formatting
- Refactor: Untuk refactoring kode
- Test: Untuk menambah atau memperbaiki test
- Chore: Untuk maintenance tasks