PGDMP         ;        	        z         
   tokomainan    14.2    14.2     ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ?           1262    16468 
   tokomainan    DATABASE     m   CREATE DATABASE tokomainan WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Indonesian_Indonesia.1252';
    DROP DATABASE tokomainan;
                postgres    false            ?            1259    16489    customer    TABLE     ?   CREATE TABLE public.customer (
    idcus integer NOT NULL,
    nama character varying(50) NOT NULL,
    mainan character varying(50) NOT NULL,
    jumlah integer NOT NULL,
    harga integer NOT NULL
);
    DROP TABLE public.customer;
       public         heap    postgres    false            ?            1259    16488    customer_idcus_seq    SEQUENCE     ?   CREATE SEQUENCE public.customer_idcus_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.customer_idcus_seq;
       public          postgres    false    210            ?           0    0    customer_idcus_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.customer_idcus_seq OWNED BY public.customer.idcus;
          public          postgres    false    209            \           2604    16492    customer idcus    DEFAULT     p   ALTER TABLE ONLY public.customer ALTER COLUMN idcus SET DEFAULT nextval('public.customer_idcus_seq'::regclass);
 =   ALTER TABLE public.customer ALTER COLUMN idcus DROP DEFAULT;
       public          postgres    false    209    210    210            ?          0    16489    customer 
   TABLE DATA           F   COPY public.customer (idcus, nama, mainan, jumlah, harga) FROM stdin;
    public          postgres    false    210   2       ?           0    0    customer_idcus_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.customer_idcus_seq', 2, true);
          public          postgres    false    209            ^           2606    16496    customer customer_nama_key 
   CONSTRAINT     U   ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_nama_key UNIQUE (nama);
 D   ALTER TABLE ONLY public.customer DROP CONSTRAINT customer_nama_key;
       public            postgres    false    210            `           2606    16494    customer customer_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_pkey PRIMARY KEY (idcus);
 @   ALTER TABLE ONLY public.customer DROP CONSTRAINT customer_pkey;
       public            postgres    false    210            ?   1   x?3?JLKKL?QpI??T?-ͩLL??N-HIM?4?46 ?=... >?&     