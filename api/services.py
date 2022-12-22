import django_rq


def create_checks(order):
    """Функція створення pdf-файлів чеків для кухні та для клієнта."""
    queue_1 = django_rq.get_queue('default')
    queue_1.enqueue(
        'api.tasks.pdf_generation',
        order_data=order,
        check_type='kitchen_check'
    )
    queue_2 = django_rq.get_queue('default')
    queue_2.enqueue(
        'api.tasks.pdf_generation',
        order_data=order,
        check_type='client_check'
    )
