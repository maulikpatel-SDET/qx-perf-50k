"""Service module 44410: business logic, no crypto."""


def calculate_total_44410(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44410():
    return 'module 44410 handles orders and invoices'
