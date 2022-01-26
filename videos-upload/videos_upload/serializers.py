from rest_framework import serializers
from .models import Videos


class VideosSerializer(serializers.ModelSerializer):

    description = serializers.CharField(required=False)

    class Meta:
        model = Videos
        fields = (
            'id',
            'name',
            'net_type',
            'ip',
            'subnet_id',
            'port_id',
            'provider',
            'status',
            'status_desc',
            'description',
            'tenant_id',
            'tenant_name',
            'created_at'
        )


class LoadBalanceListenerSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=False)
    name = serializers.CharField(required=False)
    lb_id = serializers.UUIDField(required=False)
    protocol = serializers.CharField(required=False)
    port = serializers.IntegerField(required=False)
    type = serializers.CharField(required=False)
    pip = serializers.CharField(required=False)
    ssl_id = serializers.UUIDField(required=False)
    algorithm = serializers.CharField(required=False)
    status = serializers.CharField(required=False)
    status_desc = serializers.CharField(required=False)

    class Meta:
        model = LoadBalanceListener
        fields = (
            'id',
            'name',
            'lb_id',
            'protocol',
            'port',
            'type',
            'pip',
            'ssl_id',
            'algorithm',
            'status',
            'status_desc'
        )


class LoadBalanceHostSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=False)
    name = serializers.CharField(required=False)
    listener_id = serializers.UUIDField(required=False)
    host = serializers.CharField(required=False)
    match_type = serializers.CharField(required=False)

    class Meta:
        model = LoadBalanceHost
        fields = (
            'id',
            'name',
            'listener_id',
            'host',
            'match_type'
        )


class LoadBalancePathSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=False)
    name = serializers.CharField(required=False)
    host_id = serializers.UUIDField(required=False)
    path = serializers.CharField(required=False)
    algorithm = serializers.CharField(required=False)
    match_type = serializers.CharField(required=False)

    class Meta:
        model = LoadBalancePath
        fields = (
            'id',
            'name',
            'host_id',
            'path',
            'algorithm',
            'match_type'
        )


class LoadBalanceMemberSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=False)
    p_id = serializers.UUIDField(required=False)
    ip = serializers.CharField(required=False)
    port = serializers.IntegerField(required=False)
    weight = serializers.IntegerField(required=False)

    class Meta:
        model = LoadBalanceMember
        fields = (
            'id',
            'p_id',
            'ip',
            'port',
            'weight'
        )


class SSLSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    scope = serializers.CharField(required=False)
    cert_type = serializers.CharField(required=False)
    domain = serializers.CharField(required=False)
    cert = serializers.CharField(required=False)
    pkey = serializers.CharField(required=False)
    status = serializers.CharField(required=False)
    cert_begin_time = serializers.CharField(required=False)
    cert_end_time = serializers.CharField(required=False)
    tenant_id = serializers.UUIDField(required=False)
    tenant_name = serializers.CharField(required=False)

    class Meta:
        model = SSL
        fields = (
            'id',
            'name',
            'scope',
            'cert_type',
            'domain',
            'cert',
            'pkey',
            'status',
            'cert_begin_time',
            'cert_end_time',
            'tenant_id',
            'tenant_name'
        )
