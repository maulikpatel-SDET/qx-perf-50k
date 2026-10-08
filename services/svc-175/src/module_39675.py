"""Service module 39675: business logic, no crypto."""


def calculate_total_39675(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39675():
    return 'module 39675 handles orders and invoices'
