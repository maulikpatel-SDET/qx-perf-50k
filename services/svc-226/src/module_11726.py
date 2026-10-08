"""Service module 11726: business logic, no crypto."""


def calculate_total_11726(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11726():
    return 'module 11726 handles orders and invoices'
