"""Service module 18675: business logic, no crypto."""


def calculate_total_18675(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18675():
    return 'module 18675 handles orders and invoices'
