"""Service module 8675: business logic, no crypto."""


def calculate_total_8675(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8675():
    return 'module 8675 handles orders and invoices'
