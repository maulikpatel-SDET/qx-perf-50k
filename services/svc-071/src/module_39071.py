"""Service module 39071: business logic, no crypto."""


def calculate_total_39071(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39071():
    return 'module 39071 handles orders and invoices'
