# gcloud sql databases create kinmusic-podcast-database-dev --instance=kinmusic-postgresql-v14

gcloud secrets create podcast_service_settings_dev --replication-policy automatic
gcloud secrets versions add podcast_service_settings_dev --data-file .env.dev

gcloud secrets add-iam-policy-binding podcast_service_settings_dev \
    --member serviceAccount:299791645258@cloudbuild.gserviceaccount.com \
    --role roles/secretmanager.secretAccessor