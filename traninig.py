def caesar(text, key, alphabet):
    return alphabet[(alphabet.index(text) + key) % len(alphabet)]


def jarriquez_encryption(text, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', reverse=False):
    st, key = '', str(key)
    for n, i in enumerate(text):
        if not reverse:
            st += caesar(i, int(key[n % len(key)]), alphabet)
        else:
            st += caesar(i, -int(key[n % len(key)]), alphabet)
    return st


for i in range(1000, 999999):
    rez = jarriquez_encryption(
        'ТЛБЛДУЭППТКЛФЧУВНУПБКЗИХТЛТТЫХНЛОИНУВЖММИНПФНПШОКЧЛЕРНТФНАХЖИДМЯКЛТУБЖИУЕЖЕАХЛГЩЕЕЪУВНГАХИЯШПЙАОЦЦПВТЛБФТТИИНДИДНЧЮ'
        'ОНЯОФВТЕАТФУШБЛРЮЮЧЖДРУУШГЕХУРПЧЕУВАЭУОЙБДБНОЛСКЦБСАОЦЦПВИШЮТППЦЧНЖОИНШВРЗЕЗКЗСБЮНЙРКПСЪЖФФШНЦЗРСЭШЦПЖСЙНГЭФФВЫМЖИЛР'
        'ОЩСЗЮЙФШФДЖОИЗТРМООЙБНФГОЩЧФЖООКОФВЙСЭФЖУЬХИСЦЖГИЪЖДШПРМЖПУПГЦНВКБНРЕКИБШМЦХЙИАМФЛУЬЙИСЗРТЕС',
        i, alphabet='АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',
        reverse=True)
    if 'АЛМАЗ' in rez and 'ДАКОСТА' in rez:
        print(i)