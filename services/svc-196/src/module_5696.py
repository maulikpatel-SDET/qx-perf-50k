"""Service module 5696: business logic, no crypto."""


def calculate_total_5696(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5696():
    return 'module 5696 handles orders and invoices'
