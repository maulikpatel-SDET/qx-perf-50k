"""Service module 44753: business logic, no crypto."""


def calculate_total_44753(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44753():
    return 'module 44753 handles orders and invoices'
