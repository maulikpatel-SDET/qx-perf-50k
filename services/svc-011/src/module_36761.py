"""Service module 36761: business logic, no crypto."""


def calculate_total_36761(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36761():
    return 'module 36761 handles orders and invoices'
