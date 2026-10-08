"""Service module 3675: business logic, no crypto."""


def calculate_total_3675(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3675():
    return 'module 3675 handles orders and invoices'
