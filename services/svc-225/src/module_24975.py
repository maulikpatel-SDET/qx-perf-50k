"""Service module 24975: business logic, no crypto."""


def calculate_total_24975(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24975():
    return 'module 24975 handles orders and invoices'
