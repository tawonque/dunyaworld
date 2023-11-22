# Configure the Google Cloud provider
provider "google" {
  project = "dunya-world"
  region  = "europe-west2"
}

# Create a GCS bucket
resource "google_storage_bucket" "geospatial-landing" {
  name          = "geospatial-landing"
  location      = "EU"
  force_destroy = true
}

# Create a GCS bucket
resource "google_storage_bucket" "geospatial-staging" {
  name          = "geospatial-landing"
  location      = "EU"
  force_destroy = true
}

# Create a Cloud Composer environment
resource "google_composer_environment" "dunya-geospatial" {
  name   = "dunya-geospatial"
  region = "europe-west2"

  config {
    node_count = 3

    software_config {
      image_version = "composer-2.5.1-airflow-2.6.3"
    }
  }
}