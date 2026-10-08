"""Service module 7872: business logic, no crypto."""


def calculate_total_7872(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7872():
    return 'module 7872 handles orders and invoices'
