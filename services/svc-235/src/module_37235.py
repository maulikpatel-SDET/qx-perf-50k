"""Service module 37235: business logic, no crypto."""


def calculate_total_37235(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37235():
    return 'module 37235 handles orders and invoices'
