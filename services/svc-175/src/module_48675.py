"""Service module 48675: business logic, no crypto."""


def calculate_total_48675(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48675():
    return 'module 48675 handles orders and invoices'
