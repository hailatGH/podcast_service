gcloud sql databases create kinmusic-podcast-database --instance=kinmusic-postgresql-v14

gcloud secrets create podcast_service_settings --replication-policy automatic
gcloud secrets versions add podcast_service_settings --data-file .env

gcloud secrets add-iam-policy-binding analytics_service_settings \
    --member serviceAccount:299791645258@cloudbuild.gserviceaccount.com \
    --role roles/secretmanager.secretAccessor