"""Service module 37761: business logic, no crypto."""


def calculate_total_37761(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37761():
    return 'module 37761 handles orders and invoices'
