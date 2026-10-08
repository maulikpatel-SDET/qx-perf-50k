"""Service module 31235: business logic, no crypto."""


def calculate_total_31235(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31235():
    return 'module 31235 handles orders and invoices'
