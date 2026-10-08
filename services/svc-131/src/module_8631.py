"""Service module 8631: business logic, no crypto."""


def calculate_total_8631(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8631():
    return 'module 8631 handles orders and invoices'
