"""Service module 30562: business logic, no crypto."""


def calculate_total_30562(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30562():
    return 'module 30562 handles orders and invoices'
