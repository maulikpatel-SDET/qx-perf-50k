"""Service module 30675: business logic, no crypto."""


def calculate_total_30675(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30675():
    return 'module 30675 handles orders and invoices'
