"""Service module 35675: business logic, no crypto."""


def calculate_total_35675(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35675():
    return 'module 35675 handles orders and invoices'
