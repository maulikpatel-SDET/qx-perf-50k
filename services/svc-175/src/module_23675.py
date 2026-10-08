"""Service module 23675: business logic, no crypto."""


def calculate_total_23675(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23675():
    return 'module 23675 handles orders and invoices'
