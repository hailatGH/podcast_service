from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import  CategoriesModel, EpisodesModel, SeasonsModel, HostsModel,PodcastsModel

######################################################################################################
@registry.register_document
class EpisodesmodelDocument(Document):
    season = fields.ObjectField( properties={
        "id": fields.IntegerField(),
        "season_name": fields.TextField(),
        "season_rating": fields.IntegerField(),
        "season_status": fields.BooleanField(),
        "season_releaseDate":fields.DateField(),
        "season_description": fields.TextField(),
        "season_viewcount": fields.IntegerField(),
        #"season_coverImage": fields.TextField(),
        "season_price":fields.IntegerField(),
        "encoder_FUI": fields.TextField(),
        "created_at":fields.DateField(),
        "updated_at":fields.DateField(),
        #"podcast":fields.ObjectField( properties={})
        }, 
    
    )
    host = fields.ObjectField(properties={
        "id": fields.IntegerField(),
        "host_name": fields.TextField(), 
        "host_title": fields.TextField(),
        "host_rating": fields.IntegerField(),
        "host_status": fields.BooleanField(),
        "host_description": fields.TextField(),
        "host_viewcount": fields.IntegerField(),
        #"host_profileImage": fields.TextField(),
        "host_FUI": fields.TextField(),
        "encoder_FUI": fields.TextField(),
        "created_at":fields.DateField(),
        "updated_at":fields.DateField(),
        }

    )
    category = fields.ObjectField(properties={
        "id": fields.IntegerField(),
        "category_name": fields.TextField(),
        "category_rating": fields.IntegerField(),
        "category_status": fields.BooleanField(),
        "category_description": fields.TextField(),
        "category_viewcount": fields.IntegerField(),
        #"category_coverImage": fields.TextField(),
        "encoder_FUI": fields.TextField(),
        "created_at":fields.DateField(),
        "updated_at":fields.DateField(),
    },
    
    )
    podcast = fields.ObjectField(properties={
        "id": fields.IntegerField(),
        "podcast_name": fields.TextField(),
        "podast_rating": fields.IntegerField(),
        "podcast_status": fields.BooleanField(),
        "podcast_description": fields.TextField(),
        "podcast_viewcount": fields.IntegerField(),
        #"podcast_coverImage": fields.TextField(),
        "encoder_FUI": fields.TextField(),
        "created_at":fields.DateField(),
        "updated_at":fields.DateField(),
    },
    
    )
    
    class Index:
        name = "podcast_episode"
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }


    class Django:
        model = EpisodesModel
        related_models = [CategoriesModel, PodcastsModel, SeasonsModel, HostsModel]

        fields = [
            "id",
            "episode_name",
            "episode_rating",
            "episode_status",
            "episode_releaseDate",
            "episode_description",
            "episode_viewcount",
            "episode_coverImage",
            "episode_audioFile",
            "episode_price",
            "encoder_FUI",
            "created_at",
            "updated_at"
        ]
    
    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, CategoriesModel):
            return related_instance.episode_category.all()
        elif isinstance(related_instance, PodcastsModel):
            return related_instance.episode_podcast.all()
        elif isinstance(related_instance, SeasonsModel):
            return related_instance.episode_season.all() 
        elif isinstance(related_instance, HostsModel):
            return related_instance.episode_host.all()   


######################################################################################################
@registry.register_document
class HostDocument(Document):
    # season_host= fields.ObjectField( properties={
    #     "id": fields.IntegerField(),
    #     "season_name": fields.TextField(),
    #     "season_rating": fields.IntegerField(),
    #     "season_status": fields.BooleanField(),
    #     "season_releasedate":fields.DateField(),
    #     "season_description": fields.TextField(),
    #     "season_price":fields.IntegerField(),
    #     "season_viewcount": fields.IntegerField(),
    #     "season_coverimage": fields.TextField(),
    #     "encoder_fui": fields.TextField(),
    #     "created_at":fields.DateField(),
    #     "updated_at":fields.DateField(),
    # }, )
    
    podcast_host = fields.ObjectField(properties={
        "id": fields.IntegerField(),
        "podcast_name": fields.TextField(),
        "podast_rating": fields.IntegerField(),
        "podcast_status": fields.BooleanField(),
        "podcast_description": fields.TextField(),
        "podcast_viewcount": fields.IntegerField(),
        #"podcast_coverImage": fields.TextField(),
        "podcast_description": fields.TextField(),
        "encoder_FUI": fields.TextField(),
        "created_at":fields.DateField(),
        "updated_at":fields.DateField(),
    },
    
    )
    episode_host = fields.ObjectField( properties={
        "id": fields.IntegerField(),
        "episode_name": fields.TextField(),
        "episode_rating": fields.IntegerField(),
        "episode_status": fields.BooleanField(),
        "episode_releaseDate":fields.DateField(),
        "episode_description": fields.TextField(),
        "episode_viewcount": fields.IntegerField(),
        #"episode_coverImage": fields.TextField(),
        #"episode_audioFile": fields.TextField(),
        "episode_price":fields.IntegerField(),
        "encoder_FUI": fields.TextField(),
        "created_at":fields.DateField(),
        "updated_at":fields.DateField(),
    }, )
    

    class Index:
        name = "podcast_host"
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }


    class Django:
        model = HostsModel
        related_models = [PodcastsModel, EpisodesModel,]
        fields =[
        "id",
        "host_name", 
        "host_title",
        "host_rating",
        "host_status",
        "host_description",
        "host_viewcount",
        #"host_profileImage",
        "host_FUI",
        "encoder_FUI",
        "created_at",
        "updated_at"
            ]
        
                
    def get_instances_from_related(self, related_instance):

        if isinstance(related_instance, PodcastsModel):
            return related_instance.host
        elif isinstance(related_instance, EpisodesModel):
            return related_instance.host


######################################################################################################
@registry.register_document
class SeasonDocument(Document):
    # host = fields.ObjectField(properties={
    #     "id": fields.IntegerField(),
    #     "host_name": fields.TextField(), 
    #     "host_title": fields.TextField(),
    #     "host_rating": fields.IntegerField(),
    #     "host_status": fields.BooleanField(),
    #     "host_description": fields.TextField(),
    #     "host_viewcount": fields.IntegerField(),
    #     "host_profileimage": fields.TextField(),
    #     "host_fui": fields.TextField(),
    #     "encoder_fui": fields.TextField(),
    #     "created_at":fields.DateField(),
    #     "updated_at":fields.DateField(),
    #     }

    # )
    episode_season = fields.ObjectField( properties={
        "id": fields.IntegerField(),
        "episode_name": fields.TextField(),
        "episode_rating": fields.IntegerField(),
        "episode_status": fields.BooleanField(),
        "episode_releasedate":fields.DateField(),
        "episode_description": fields.TextField(),
        "episode_viewcount": fields.IntegerField(),
        #"episode_coverImage": fields.TextField(),
        #"episode_audioFile": fields.TextField(),
        "episode_price":fields.IntegerField(),
        "encoder_FUI": fields.TextField(),
        "created_at":fields.DateField(),
        "updated_at":fields.DateField(),
    }, )
    
    podcast = fields.ObjectField(properties={
        "id": fields.IntegerField(),
        "podcast_name": fields.TextField(),
        "podast_rating": fields.IntegerField(),
        "podcast_status": fields.BooleanField(),
        "podcast_description": fields.TextField(),
        "podcast_viewcount": fields.IntegerField(),
        #"podcast_coverImage": fields.TextField(),
        "podcast_description": fields.TextField(),
        "encoder_FUI": fields.TextField(),
        "created_at":fields.DateField(),
        "updated_at":fields.DateField(),
    },
    
    )
    class Index:
        name = "podcast_season"
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }


    class Django:
        model = SeasonsModel
        related_models = [EpisodesModel, PodcastsModel]
        
        fields = [
        "id",
        "season_name",
        "season_rating",
        "season_status",
        "season_releaseDate",
        "season_description",
        "season_price",
        "season_viewcount",
        "season_coverImage",
        "encoder_FUI",
        "created_at",
        "updated_at",
        ]
        
    def get_instances_from_related(self, related_instance):

        if isinstance(related_instance, PodcastsModel):
            return related_instance.season_podcast.all()
        elif isinstance(related_instance, EpisodesModel):
            return related_instance.season

######################################################################################################
@registry.register_document
class PodcastsDocument(Document):
    category = fields.ObjectField(properties={
        "id": fields.IntegerField(),
        "category_name": fields.TextField(),
        "category_rating": fields.IntegerField(),
        "category_status": fields.BooleanField(),
        "category_description": fields.TextField(),
        "category_viewcount": fields.IntegerField(),
        #"category_coverImage": fields.TextField(),
        "category_description": fields.TextField(),
        "encoder_FUI": fields.TextField(),
        "created_at":fields.DateField(),
        "updated_at":fields.DateField(),
    },
    
    )
    host = fields.ObjectField(properties={
        "id": fields.IntegerField(),
        "host_name": fields.TextField(), 
        "host_title": fields.TextField(),
        "host_rating": fields.IntegerField(),
        "host_status": fields.BooleanField(),
        "host_description": fields.TextField(),
        "host_viewcount": fields.IntegerField(),
        #"host_profileImage": fields.TextField(),
        "host_FUI": fields.TextField(),
        "encoder_FUI": fields.TextField(),
        "created_at":fields.DateField(),
        "updated_at":fields.DateField(),
        }

    )
    episode_podcast = fields.ObjectField( properties={
        "id": fields.IntegerField(),
        "episode_name": fields.TextField(),
        "episode_rating": fields.IntegerField(),
        "episode_status": fields.BooleanField(),
        "episode_releaseDate":fields.DateField(),
        "episode_description": fields.TextField(),
        "episode_viewcount": fields.IntegerField(),
        #"episode_coverImage": fields.TextField(),
        #"episode_audioFile": fields.TextField(),
        "episode_price":fields.IntegerField(),
        "encoder_FUI": fields.TextField(),
        "created_at":fields.DateField(),
        "updated_at":fields.DateField(),
    }, )
    season_podcast = fields.ObjectField( properties={
        "id": fields.IntegerField(),
        "season_name": fields.TextField(),
        "season_rating": fields.IntegerField(),
        "season_status": fields.BooleanField(),
        "season_releaseDate":fields.DateField(),
        "season_description": fields.TextField(),
        "season_viewcount": fields.IntegerField(),
        #"season_coverImage": fields.TextField(),
        "season_price":fields.IntegerField(),
        "encoder_FUI": fields.TextField(),
        "created_at":fields.DateField(),
        "updated_at":fields.DateField(),
    }, )


    class Index:
        name = "podcast_podcasts"
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }


    class Django:
        model = PodcastsModel
        related_models = [CategoriesModel, EpisodesModel, SeasonsModel, HostsModel]
        fields = [
        "id",
        "podcast_name",
        "podcast_rating",
        "podcast_status",
        "podcast_description",
        "podcast_viewcount",
        "podcast_coverImage",
        "encoder_FUI",
        "created_at",
        "updated_at",
        ]
    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, CategoriesModel):
            return related_instance.podcast_category.all()
        elif isinstance(related_instance, EpisodesModel):
            return related_instance.podcast
        elif isinstance(related_instance, SeasonsModel):
            return related_instance.podcast 
        elif isinstance(related_instance, HostsModel):
            return related_instance.podcast_host.all()   

######################################################################################################
@registry.register_document
class CategoryDocument(Document):
    podcast_category = fields.ObjectField(properties={
        "id": fields.IntegerField(),
        "podcast_name": fields.TextField(),
        "podast_rating": fields.IntegerField(),
        "podcast_status": fields.BooleanField(),
        "podcast_description": fields.TextField(),
        "podcast_viewcount": fields.IntegerField(),
        #"podcast_coverImage": fields.TextField(),
        "podcast_description": fields.TextField(),
        "encoder_FUI": fields.TextField(),
        "created_at":fields.DateField(),
        "updated_at":fields.DateField(),
    },
    
    )
    episode_category = fields.ObjectField( properties={
        "id": fields.IntegerField(),
        "episode_name": fields.TextField(),
        "episode_rating": fields.IntegerField(),
        "episode_status": fields.BooleanField(),
        "episode_releaseDate":fields.DateField(),
        "episode_description": fields.TextField(),
        "episode_viewcount": fields.IntegerField(),
        #"episode_coverImage": fields.TextField(),
        #"episode_audioFile": fields.TextField(),
        "episode_price":fields.IntegerField(),
        "encoder_FUI": fields.TextField(),
        "created_at":fields.DateField(),
        "updated_at":fields.DateField(),
    }, )


    class Index:
        name = "podcast_category"
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }


    class Django:
        model = CategoriesModel
        related_models = [ EpisodesModel]
        fields = [
        "id",
        "category_name",
        "category_rating",
        "category_status",
        "category_description",
        "category_viewcount",
        "category_coverImage",
        "encoder_FUI",
        "created_at",
        "updated_at",
        ]
    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, EpisodesModel):
            return related_instance.category
        elif isinstance(related_instance, PodcastsModel):
            return related_instance.category 
#python manage.py inspectdb --database=podcast_db > models.py