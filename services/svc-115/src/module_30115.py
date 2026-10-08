"""Service module 30115: business logic, no crypto."""


def calculate_total_30115(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30115():
    return 'module 30115 handles orders and invoices'
