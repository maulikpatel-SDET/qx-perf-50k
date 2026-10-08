"""Service module 39772: business logic, no crypto."""


def calculate_total_39772(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39772():
    return 'module 39772 handles orders and invoices'
