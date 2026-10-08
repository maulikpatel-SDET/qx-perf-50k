"""Service module 44020: business logic, no crypto."""


def calculate_total_44020(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44020():
    return 'module 44020 handles orders and invoices'
